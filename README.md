# Quality Metrics for Agent Trajectories
### This is a repository containing solutions of three tasks for the "Quality Metrics for Agent Trajectories" internship.
## Task 1
I've used the Docent API to get each Agent Run's transcript in the GPT-5-2 Codex collection. Authentication is handled through a local environment file containing the Docent API KEY.
## Task 2
I've collected data of all trajectories for the mentioned top 5 models. 
I observed that almost every run contains exactly one user and one system message, while the majority of interaction volume comes from alternating tool and assistant calls. Most runs are relatively balanced, with the number of assistant messages typically differing from tool messages by only 0–3 interactions suggesting iterative tool-use reasoning loops rather than long standalone responses.


The median trajectory length falls roughly between 70 and 100 total messages, with many runs being around 70–90 messages. Examples include totals of 71, 74, 83, 87, and 91 messages across the collections. 
However, the variance is high. Some trajectories are short (29–40 messages), while several outliers exceed 200 messages.

The most significant outlier observed is a trajectory containing 319 total messages (158 tool, 159 assistant), indicating a very long reasoning chain or repeated tool-calling behavior. Other large outliers are runs with 283, 279, 241, 227, and 222 messages. In contrast, the shortest trajectories contain only around 29–39 messages.

Different models also appear to have different trajectory styles. For example, the claude-4-5-opus-high collection generally shows shorter and more compact trajectories, frequently between 40 and 84 total messages. At the same time, some other collections contain substantially deeper tool-usage chains with repeated rather high outliers above 150 messages. 
Overall, the data suggests that the primary difference between models is not the number of user/system interactions, but rather how strongly they rely on iterative assistant-tool exchanges.
## Task 3
