# Quality Metrics for Agent Trajectories
### This is a repository containing solutions of three tasks for the "Quality Metrics for Agent Trajectories" internship.
I explain tasks 2 and 3 here as well as on Your [website](https://internship.jetbrains.com). In addition, I've attached a pdf copy of the research paper with my highlightes and notes as a proof of my independent work.
## Task 1
I've used the Docent API to get each Agent Run's transcript in the GPT-5-2 Codex collection. Authentication is handled through a local environment file containing the Docent API KEY.
## Task 2
I've collected data of all trajectories for the mentioned top 5 models.  
I've observed that almost every run contains exactly one user and one system message, while the majority of interaction volume comes from alternating tool and assistant calls. Most runs are relatively balanced, with the number of assistant messages typically differing from tool messages by only 0–3 interactions suggesting iterative tool-use reasoning loops rather than long standalone responses.

The median trajectory length falls roughly between 70 and 100 total messages, with many runs being around 70–90 messages. Examples include totals of 71, 74, 83, 87, and 91 messages across the collections. 
However, the variance is high. Some trajectories are short (29–40 messages), while several outliers exceed 200 messages.

The most significant outlier observed is a trajectory containing 319 total messages (158 tool, 159 assistant), indicating a very long reasoning chain or repeated tool-calling behavior. Other large outliers are runs with 283, 279, 241, 227, and 222 messages. In contrast, the shortest trajectories contain only around 29–39 messages.

Different models also appear to have different trajectory styles. For example, the claude-4-5-opus-high collection generally shows shorter and more compact trajectories, frequently between 40 and 84 total messages. At the same time, some other collections contain substantially deeper tool-usage chains with repeated rather high outliers above 150 messages.  
Overall, the data suggests that the primary difference between models is not the number of user/system interactions, but rather how strongly they rely on iterative assistant-tool exchanges.
## Task 3
### Summary
In other domains like aviation, nuclear power, automotive or railway systems there has been a way to describe reliable and safe systems as a multi-dimensional quality. Similarly, the authors of the paper are trying to expand this definition in current AI agents. A single “90% accuracy” score hides all of important information, since reliability, in their definition, is multidimensional.

The safety-critical perspective to agent evaluations described in their work **divides reliability into four dimensions**:

1. <ins>Consistency</ins>: Does the system behave the same expected way across different runs?
   Even acceptable average performance becomes problematic when high variance makes outcomes unpredictable.
2. <ins>Robustness</ins>: Under different conditions, does the system degrade gradually or fail out of a sudden?
   Graceful degradation is better than abrupt failure.
3. <ins>Predictability</ins>: Can it predict its failure?
   Users should be able to expect whether the agent will fail or succeed.
4. <ins>Safety</ins>: When failures occur, how bad are the resulting consequences?
   Agents that take actions on their own can cause real harm.

Each dimension captures a property that matters for deployment but cannot be measured by accuracy alone. Later in chapter 3 authors aggregate reliability metrics within each dimension and compute an **overall reliability score** excluding safety, as they state "_Safety violations are inherently a tail phenomenon: what matters is not average safety but the presence of any severe violations. An agent that behaves safely 99% of the time but causes catastrophic harm in 1% of cases should not receive a high safety score simply because harmful events are rare._".

Across these dimensions, the authors provide a performance profile that consist of 12 metrics and 4 dimenisions describing 14 models within two benchmarks.

The scientists analyze how reliability changes with task difficulty in the **GAIA benchmark**. They expected medium-difficulty tasks to produce the most inconsistent results, but instead found that consistency usually changes steadily as tasks become harder. More challenging tasks also made resource usage less predictable, especially in newer Claude models that tend to use more actions on hard problems. Predictability generally worsened slightly with task difficulty, while robustness showed no clear connection to difficulty.

In **τ-bench**, the authors focus on safety in customer-service-style interactions. They test whether agents follow important rules, such as verifying identity and preventing unauthorized actions. They found that financial reasoning mistakes were the most common safety issue. Although serious violations were rare in advanced models, even small numbers of high-severity failures could still be dangerous in real-world settings.

They also discuss errors in the τ-bench benchmark itself. After removing incorrect tasks, predictability and safety scores improved for most agents, especially calibration. This showed that poor benchmark quality can unfairly affect reliability evaluation results.

Last three chapters contain recommendations, limitations and a short conclusion with a mention for future work. The authors explain what they believe the AI field should do next in order to build trustworthy AI agents. Their main argument is that current evaluation methods focus too heavily on whether an AI system can complete a task successfully, while ignoring whether it can do so consistently, safely and predictably. According to the authors, this creates a misleading picture of progress because strong benchmark performance doesn't necessarily mean that a system is dependable in real-world situations.

They provide four **recommendations**; Their experiments showed that many AI agents perform well on tasks but still fail unpredictably, behave inconsistently across repeated attempts, or break when conditions change slightly. Because of this, they argue that reliability should become its own area of scientific study with dedicated metrics and evaluation methods.

Current benchmarks are critized for being too controlled and simplistic. Many evaluations only test a single run of a task, even though real-world environments contain uncertainty and changing situations. To address this, the authors recommend evaluating systems repeatedly, using variations in prompts and environments to measure how stable the agents really are. 

They also emphasize that reliability cannot be reduced to a single number. Through their evaluations, they found that AI agents can perform very differently. A system might appear highly capable but still be fragile, unsafe or overconfident. Because of this, they recommend evaluating reliability using multiple dimensions mentioned earlier.

Safety is another central concern in this chapter. The authors argue that failures are inevitable in complex AI systems, so the goal is never perfection. Instead AI agents should fail in controlled and understandable ways that minimize harm. This is particularly important for autonomous agents that can interact with tools or make decisions without human supervision.

Overall the recommendations chapter reflects the authors’ belief that AI research needs to become more mature and engineering-oriented. They argue that the field currently focuses too much on rapid progress and benchmark competition, while not paying enough attention to long-term reliability and safety.

The authors acknowledge that their work is only an early step toward understanding AI reliability. They do not present their framework as a complete solution, but rather as a starting point for future research. They are careful to point out the **limitations** of their approach and address <ins>two potential objections</ins>.

Reliability itself is still difficult to define precisely. The authors explain that there is no universally accepted definition of AI reliability, and different researchers may disagree about which properties matter most. They admit that no set of metrics can capture every possible failure mode of an autonomous AI agent. Some failures may be extremely rare or emerge only in complex situations that are difficult to reproduce systematically. They know that AI systems evolve extremely quickly, meaning that the specific models they evaluated may soon become outdated. They also recognize that their experiments are still based on benchmarks and controlled testing environments. 

Authors tell in their **conclusion** that AI agents are becoming more capable much faster than they are becoming reliable. This is the paper’s main idea: capability alone is not enough to justify trust in AI systems. Their evaluations showed that even highly capable agents can still fail in surprising and inconsistent ways. Some systems perform well in one situation but collapse under small changes in prompts or environments. They believe reliability is fundamentally multidimensional and AI research currently prioritizes rapid capability improvements and benchmark competition over deeper questions about safety and dependability. They argue that this approach is dangerous, especially as autonomous agents gain the ability to interact with real systems and make increasingly important decisions.

### Main findings of the work
From figures 2 and 3 we learn that the GAIA and τ-bench benchmarks show that model consistency is still limited, even in advanced frontier models. Many agents are also sensitive to small prompt changes, with only slight and unreliable improvements in newer models.

The figure at the beginning of the paper (1) proves that despite 18 months of model development, overall reliability only shows small improvements over time. They are also disproportionate across evaluation scenarios: τ-bench shows moderate gains, while GAIA shows barely any improvement, and that's even among latest models. They explain that because of more complicated structure of τ-bench consistent behaviour is easier to achieve. With GAIA's open questions, it is the other way around, although other factors may also contribute. Scientists propose that improving raw task performance may not be sufficient for building dependable AI agents. 

They also provide **dimension-specific findings**:

The outcome <ins>consistency</ins> remains low across all models, which means agents that can solve a task often fail to do so regularly. They reliably select similar action types across runs but vary in execution order. Resource consistency results reveal high variance in token and compute usage across runs, especially on GAIA.

<ins>Robustness</ins> analysis reveals an asymmetry in model vulnerabilities. Models handle genuine technical failures gracefully yet remain vulnerable to surface-level variations in task specifications.

<ins>Predictability</ins>: calibration, on which many initial models fell short, has improved noticeably in recent models (especially Claude ones on both benchmarks). In contrast, discrimination trends are different across benchmarks: on τ-bench, it has generally improved in recent models, but on GAIA it has mostly worsened.

<ins>Security</ins>: Recent frontier models exhibit markedly lower violation rates with the most capable models from each provider achieving the highest compliance scores. Harm severity scores are generally high across the board, indicating that when violations happen, most are low-to-moderate in severity.

Authors also observe that reliability doesn't scale equally with model capability. While calibration, robustness, and safety generally improve with model size within families, consistency often works the other way around: smaller models rather achieve equal or higher consistency than their larger counterparts. They also mention that reasoning models are generally more reliable than the non-reasoning ones.

The authors point out an interesting observation of real-world failures from section 1: they state that each of the vulnerabilities could have been predicted through systematic evaluation using their reliability metrics.
