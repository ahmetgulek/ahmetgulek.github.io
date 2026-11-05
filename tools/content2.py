# Content for the design-A build. All narrative text is Ahmet's own: research statement Draft 16
# (2026-10-26) and the JMP-1 pitch deck (Sep 2026) / H-1B talk (Oct 27, 2026). Statuses public-safe.
NAME = "Ahmet Gulek"
TITLE = ""  # role line under the name; empty = not shown (Ahmet, 2026-11-03)
AFFIL = "Stanford Immigration Policy Lab · RFBerlin · ifo Institute"
BIO = ("I am a labor economist who brings tools from trade, industrial organization, and "
       "macroeconomics to study immigration, gender inequality, and, more recently, minimum wages. "
       "I received my PhD from MIT in 2025, where my committee consisted of Joshua Angrist, "
       "Daron Acemoglu, and Amy Finkelstein. I am currently a Postdoctoral Fellow at the Stanford "
       "Immigration Policy Lab, under the supervision of Ran Abramitzky and Jens Hainmueller. "
       "I am also an affiliate of RFBerlin and the ifo Institute. My solo-authored work has appeared "
       "in the *Journal of Development Economics*, is forthcoming in *AEA Papers and Proceedings*, "
       "and is under revision at the *Journal of Human Resources*. A coauthored paper, which I led, "
       "is forthcoming in the *Journal of Labor Economics*. I am on the 2026-2027 academic job market.")
# Ahmet's bio, 2026-11-03 (from his cover letter); *...* = italics
LINKS = [("Email", "mailto:agulek@stanford.edu"), ("CV", "CV.pdf"),
         ("LinkedIn", "https://www.linkedin.com/in/ahmet-gulek-8274816a/"),
         ("Bluesky", "https://bsky.app/profile/ahmetgulek.bsky.social"), ("Twitter / X", "https://x.com/AhmetGulekk")]

PAPERS = [
 dict(id="jmp1", sec="jmp", title="Effects of Immigrants on Non-host Regions: Evidence from Syrian Refugees in Turkey",
      coauthors="", tag="Job Market Paper 1", status="Submitted", links=[("PDF","Gulek_jmp.pdf")],
      abstract="I study how local immigration shocks impact labor markets and firms across the economy through production networks. Using Turkey's Syrian refugee crisis and firm-to-firm VAT data, I show that firms buying from host regions demand more labor, while those selling to host regions increase sales. Estimates imply an elasticity of substitution between labor and intermediates of 0.79 and across intermediates of 1.06. Spillover magnitudes depend critically on network centrality and immigrants' skills. A 1% labor supply increase in Istanbul decreases local real wages by 0.56% while increasing non-host wages by 0.38%. For non-central regions, identical shocks reduce local wages by 1% with negligible spillovers. Similarly, high-skill immigrants create larger spillovers and, therefore, larger welfare gains than low-skill immigrants because high-skill-intensive industries are more central than low-skill-intensive industries. Network position and immigrants' skills determine the extent to which immigration only lowers local wages or also generates substantial economy-wide gains."),
 dict(id="jmp2", sec="jmp", title="Long-Run Effects of H-1B Immigration on the U.S. Economy",
      coauthors="with Ran Abramitzky, Leah Boustan, and Jens Hainmueller", tag="Job Market Paper 2", status="NBER Working Paper 35560, submitted",
      links=[("PDF","Abramitzky-Boustan-Gulek-Hainmueller-H1B.pdf")],
      abstract="We study the effects of H-1B immigration on U.S. industries that employ H-1B workers and their trading partners. Using a novel cross-industry design and the 1999–2003 expansion of the H-1B visa cap for identification, we find that H-1B exposure raised incomes for natives and pre-existing immigrants, with gains concentrated in non-STEM occupations. Income gains propagate forward through supply chains to downstream industries but not backward to upstream industries, consistent with a productivity shock rather than a labor supply shock. We find no direct effect on patenting, suggesting that productivity gains arise from better task execution rather than patentable invention."),
 dict(id="colombia", sec="pub", title="Formal Effects of Informal Labor and Work Permits: Evidence from Venezuelan Refugees in Colombia",
      coauthors="with Dany Bahar and Isabel Di Tella", tag="", status="Journal of Labor Economics, forthcoming", links=[("PDF","Bahar_DiTella_Gulek_Colombia.pdf")],
      abstract="We analyze the Venezuelan refugee crisis in Colombia to separate the labor market effects of informal immigration and work permits. Using Synthetic Instrumental Variables, we find informal immigration displaced natives from both informal and formal sectors, implying high substitutability between worker types (elasticity ≈ 10). A triple difference-in-differences shows work permits reduced competition in the informal sector and raised it in the formal sector. Our model implies this created 23,100 formal jobs and roughly $42 million in annual tax revenue, which provides an economic rationale for granting refugees the right to work."),
 dict(id="pp", sec="pub", title="Where Should Refugees Go? Production Networks and the Welfare Gains from Immigrant Placement",
      coauthors="", tag="", status="AEA Papers and Proceedings, forthcoming (May 2027)", links=[], abstract=""),
 dict(id="jde", sec="pub", title="Driving While Hungry: The Effect of Fasting on Traffic Accidents",
      coauthors="", tag="", status="Journal of Development Economics, 2024", links=[("Journal","https://www.sciencedirect.com/science/article/pii/S0304387824000099")],
      abstract="I study the impact of hunger on traffic accidents by exploiting the fasting that is religiously mandated during the month of Ramadan. Identification comes from working hours not being adjusted during Ramadan in Turkey. I find that driving while fasting at rush hour is associated with a significant increase in road traffic accidents. Using existing survey evidence on fasting rates in Turkey, I conclude that hunger induced by fasting increases the probability of an accident by 25%, which is smaller than the effect of driving while intoxicated, but larger than the effect of mild sleep deprivation."),
 dict(id="feoil", sec="wp", title="Formal Effects of Informal Labor: Evidence from Syrian Refugees in Turkey",
      coauthors="", tag="", status="Revise and resubmit, Journal of Human Resources", links=[("PDF","FEoIL.pdf")],
      abstract="I study the effects of Syrian refugees, who are denied work permits and thus can only work informally, on Turkish firms and workers. Using travel distance as an instrument for refugee location, I show that low-skill natives lose both informal and formal salaried jobs. I document two mechanisms: formal firms reduce their formal labor demand and new firms do not enter the formal economy. Estimates imply an elasticity of substitution of 10 between formal and informal workers. Counterfactual exercises predict that granting refugees work permits would have created up to 120,000 formal jobs in the economy through higher informal wages."),
 dict(id="siv", sec="wp", title="Synthetic IV Estimation in Panels",
      coauthors="with Jaume Vives-i-Bastida", tag="", status="", links=[("PDF","https://jvivesb.github.io/jmp/draft_siv.pdf")],
      abstract="We propose a Synthetic Instrumental Variables (SIV) estimator for panel data that combines the strengths of instrumental variables and synthetic controls to address unmeasured confounding. We derive conditions under which SIV is consistent and asymptotically normal, even when the standard IV estimator is not. Motivated by the finite sample properties of our estimator, we introduce an ensemble estimator that simultaneously addresses multiple sources of bias and provide a permutation-based inference procedure. We demonstrate the effectiveness of our methods through a calibrated simulation exercise, two shift-share empirical applications, and an application in digital economics that includes both observational data and data from a randomized control trial. In our primary empirical application, we examine the impact of the Syrian refugee crisis on Turkish labor markets. Here, the SIV estimator reveals significant effects that the standard IV does not capture. Similarly, in our digital economics application, the SIV estimator successfully recovers the experimental estimates, whereas the standard IV does not."),
 dict(id="cpocc", sec="wp", title="Occupational Heterogeneity of Child Penalty in the United States",
      coauthors="", tag="", status="Submitted", links=[("PDF","Gulek_CP_Occupations.pdf")],
      abstract="I investigate how parenthood reshapes employment patterns across occupations and how this occupational heterogeneity contributes to earning disparities. Using a novel rotating panel approach to estimating child penalties, I document that both men and women change occupations. The well-established null effect of fatherhood hides that men's employment rate decreases in some occupations like finance and increases in others like construction. Women leave most occupations but select into occupations with part-time options. These occupational changes explain 40% of the income penalty for women, most of the income penalty for men, and most of the wage penalty for both genders."),
 dict(id="wfhcp", sec="wp", title="Effect of Remote Work on the Child Penalty: Evidence from the United States",
      coauthors="with Christina Langer", tag="", status="Submitted", links=[("PDF","Gulek_Langer_WFH_CP.pdf")],
      abstract="We study the effect of the post-COVID expansion of remote work on the child penalty. Our empirical design proceeds in three steps: using pseudo-panels to estimate child penalties across occupations, exploiting cross-occupational variation in remote work adoption, and using synthetic controls to adjust for differential pre-COVID trajectories. Remote work reduces the hours penalty for mothers: each percentage point increase in an occupation's remote work share raises mothers' hours worked by 0.19%, eliminating one-seventh of the baseline hours penalty for the average remote occupation. We find no effects on employment, income, or wages for mothers, and no average effects on men."),
 dict(id="minwage", sec="wip", title="Production Network Propagation of Minimum Wage Shocks: Evidence from Turkey",
      coauthors="", tag="", status="Draft coming soon", links=[],
      abstract="I study the 30% increase in Turkey's minimum wage in 2016 using the same administrative and survey data as my first job market paper. The minimum wage raised wages in both the formal and the informal sector, the latter because formal and informal workers are gross substitutes. Firms passed the higher labor costs through to the prices of the goods they produce. Firms more exposed to the minimum wage cut employment and exited at higher rates, and the effects propagated along the supply network: the suppliers and customers of exposed firms also shrank, the mirror image of my immigration results. Displaced workers moved to less exposed firms, especially those serving the domestic market, as customers substituted toward less exposed competitors. A production network model rationalizes these findings."),
 dict(id="canada", sec="wip", title="Immigration, Housing, and Voting: Evidence from Canada's Post-2015 Immigration Surge",
      coauthors="with Jeremy Ferwerda and Jens Hainmueller", tag="", status="", links=[],
      abstract="Canada's permanent resident admissions rose from about 270,000 in 2015 to over 480,000 in 2024, following the introduction of the Express Entry system. We study how this surge affected local rents and voting behavior, and how much of the effect on voting runs through the housing market. To identify the effect on rents, we build on the standard past-settlement instrument in two ways: we exploit the policy-induced surge in admissions, and we relax the share-exogeneity assumption embedded in the instrument using Synthetic IV. We find that immigration raises rents in regions with tight labor markets and in regions where geographic constraints make housing supply inelastic. We are currently extending the analysis to house prices, vacancies, and new construction. We will then estimate the effects on voting and use variation in housing supply elasticity to isolate the role of rents in shaping political responses to immigration."),
 dict(id="noway", sec="wip", title="No Way Back? Reallocation Frictions and Asymmetric Adjustment to Refugee Arrivals and Returns",
      coauthors="with Sarah Winton", tag="", status="Data acquisition in progress", links=[],
      abstract="The fall of the Assad regime in December 2024 triggered a large, unanticipated return of Syrian refugees from Jordan, reversing the labor supply shock their arrival created a decade earlier. Using novel returns data matched to Syrian refugees' individual work experience, skills, and credentials, we study whether host-country labor markets adjust symmetrically to refugee arrivals and departures, or whether downward wage rigidity, irreversible investments, and sectoral reallocation frictions make adjustment to departures slow and incomplete."),
 dict(id="ukfathers", sec="wip", title="Remote Work and Fathers' Long Hours: Evidence from the United Kingdom",
      coauthors="", tag="", status="Draft coming soon", links=[],
      abstract="I study how the post-pandemic expansion of remote work changed the child penalty in the United Kingdom. I estimate child penalties by occupation from the Labour Force Survey and correct for differences in pre-pandemic trends using synthetic controls. Remote work reduced the probability that fathers work long hours relative to childless men. The effect is concentrated between 38 and 49 hours a week and appears nowhere else in the hours distribution. I find no effect on mothers. This reverses the pattern in the United States, where remote work raised mothers' hours and left men unaffected."),
 dict(id="norms", sec="wip", title="Remote Work, Gender Norms, and the Child Penalty",
      coauthors="with Natalie Irmert and Christina Langer", tag="", status="", links=[],
      abstract="We test whether gender norms and family institutions shape how remote work changes the child penalty. Comparisons across countries mix up norms and institutions, so we pair them with a design inside one country that holds institutions fixed. Across roughly twenty countries, we estimate child penalties by occupation from labor force surveys and administrative data, correct for differences in pre-pandemic trends using synthetic controls, and relate the effect of remote work to pre-pandemic norms and institutions. Within Sweden, we use population registers to compare children of immigrants whose parents come from countries with different gender norms, but who share the same labor market, family policies, and employers. The registers also record parental leave and days caring for a sick child, taken by each parent. Funded by an LSE Remote and Distributed Work Research Initiative grant."),
]
SECTIONS = [("jmp","Job Market Papers"),("pub","Publications"),("wp","Working Papers"),("wip","Work in Progress")]

# kind "referenced" prints "Referenced by <outlet>"; the others print the outlet alone.
PRESS = [
 ("BBC News", "Trump's green card curbs test Indian tech workers' American dream", "https://www.bbc.com/news/articles/cqj34j7dk771o", "October 21, 2026", "quoted"),
 ("Reuters", "Explainer: The skilled foreign tech workers' green card program under attack from Trump", "https://www.reuters.com/world/skilled-foreign-tech-workers-green-card-program-under-attack-trump-2026-10-08/", "October 8, 2026", "quoted"),
 ("ITIF", "Fact of the Week: H-1B Immigration Raised Native Non-STEM Workers' Incomes by About 15 Percent in Computer Systems Design", "https://itif.org/publications/2026/09/14/h1b-immigration-raised-incomes-about-15-percent-computer-systems-design/", "September 14, 2026", "referenced"),
 ("Bloomberg Law", "H-1B Demand Plummeted in Fallout of First Trump $100,000 Fee", "https://news.bloombergtax.com/immigration/h-1b-demand-plummeted-in-fallout-from-trumps-first-100-000-fee", "September 8, 2026", "quoted"),
 ("Marginal Revolution", "The economics of H-1B immigration", "https://marginalrevolution.com/marginalrevolution/2026/08/the-economics-off-h-1b-immigration.html", "August 2026", "referenced"),
 ("Hoover Institution, Commons on Freedom Frequency", "Essay on the H-1B program, with Ran Abramitzky, Leah Boustan, and Jens Hainmueller", "", "in preparation", "essay"),
]

# ---------- Research page (rebuilt 2026-11-05 from Ahmet's own story text; typo fixes only, other edits listed in his review notes) ----------
OPENING = ("Three of the largest changes to labor markets in the last decade have been unprecedented refugee flows in developing economies, changing immigration policies in developed countries, and the COVID-induced change in where work is conducted. My research covers all three. I have worked on the Syrian and Venezuelan refugee crises, high-skill immigration policies in the US and Canada, and on how the adoption of remote work is impacting gender inequality across several countries.")  # Ahmet, 2026-11-03

TOC = [("jmp1", "JMP-1"), ("jmp2", "JMP-2"), ("refugees", "Refugee Crises"), ("remote", "Remote Work and Gender Inequality")]
SIV_URL = "https://jvivesb.github.io/jmp/draft_siv.pdf"
BLOOMBERG_URL = "https://news.bloombergtax.com/immigration/h-1b-demand-plummeted-in-fallout-from-trumps-first-100-000-fee"

# Blocks: ("banner", paper id) big JMP header; ("section", id, title) plain section header; ("h3", text);
# ("p", text) with [text](url) links and *italics*; ("fig", src, title, note); ("row", [(src, title, note), ...]) side by side;
# ("list", [items]); ("papers", heading, [ids]) expandable paper boxes; ("box", "restriction") the closing numbers box.
# Figures: file in assets/img/ or "svg:<name>". _{x} in a note prints as a subscript.
RESEARCH = [
 ("banner", "jmp1"),
 ("p", "Turkey received 3.6 million Syrian refugees, who mostly settled in the south-east regions closer to the border. Suppose we want to understand the labor market consequences of this shock. The standard approach is to assume the effects are local and compare host to non-host regions before and after the immigration shock. However, these shocks are so large that they are likely to impact the prices of goods, which can then induce general equilibrium effects across the economy. If we want to understand the effects of immigration, we need to understand the G.E. forces it triggers."),
 ("fig", "s_jmp1_map.png", "Turkey hosts 3.6 million Syrian refugees", "Number of Syrians per 100 natives in 2019."),
 ("p", "This is essentially what I do in my first job market paper. In a nutshell, I study the G.E. effects of immigration in three parts: theory, empirics, and counterfactuals. Theory characterizes the G.E. forces by which immigrants in one region impact firms in other regions. Empirically, I test the model's implications and estimate the key structural elasticities. I use counterfactuals to quantify the total effects of immigration. The main result of the paper is that when immigrants settle in large, central cities, their effects are global, not local. This intuition can guide policymakers to settle immigrants and refugees to maximize economic gains, and helps resolve a long-lasting puzzle in the immigration literature: why do we not have a consensus on how immigration impacts natives' earnings?"),
 ("h3", "Theory"),
 ("fig", "svg:network", "Naming trade spillovers", ""),
 ("list", ["i₁ supplies i₂; i₂ and i₄ supply i₃. Immigration lowers i₂'s labor costs and prices.",
           "G.E. force 1, the cost shock propagates forward: i₃ demands more (less) labor if intermediate goods and labor are gross complements (substitutes).",
           "G.E. force 2, demand spillovers from substitution among intermediates: i₃ reallocates its spending between i₂ and i₄ based on substitutability among intermediates.",
           "G.E. force 3, two forces impact i₁: i₂'s input choice between labor and i₁'s goods, and i₃'s reallocation between i₂ and i₄."]),
 ("p", "Formally, I derive these forces by adding regional labor markets to a model of production networks. This was a more impressive feat when I first wrote the model, which was pre-AI 🙂 The details can be found in the paper."),
 ("h3", "Testing the theory"),
 ("p", "I compare firms in non-host regions who follow similar trajectories before the immigration shock, who happen to be differentially exposed to immigrants through their trading partners. To do that, I combine synthetic controls with IV, a tool Jaume Vives-i-Bastida and I developed in [another paper](" + SIV_URL + ")."),
 ("row", [("s_jmp1_es_upstream.png", "Upstream exposure increases size and payroll", "Firms buying from host regions hire more workers ⇒ labor and intermediates are complements."),
          ("s_jmp1_es_downstream.png", "Firms selling to host regions sell more", "Effects of D1 and D2 exposures on sales."),
          ("s_jmp1_eos.png", "Elasticity estimates", "σ_{u} = 0.79 < 1: labor and intermediates are complements. σ_{l} = 1.06 ≈ 1: intermediates are Cobb-Douglas.")]),
 ("p", "The model is overidentified, and the data does not reject the model."),
 ("h3", "Counterfactuals"),
 ("p", "Given that spillovers exist, I ask: why should we care? How big are spillovers? I use the model to answer these questions."),
 ("fig", "s_jmp1_ge_heatmap.png", "Counterfactual 1: how big are G.E. effects?",
  "81 counterfactuals for 81 provinces: 1% increase in labor supply in the host region, then calculate the change in non-host real wages (map in basis points). Take-away: mostly negligible spillovers."),
 ("p", "A 1% labor supply increase in Istanbul decreases local real wages by 0.56% while increasing non-host wages by 0.38%. For non-central regions, identical shocks reduce local wages by 1% with negligible spillovers. Similarly, high-skill immigrants create larger spillovers and, therefore, larger welfare gains than low-skill immigrants because high-skill-intensive industries are more central than low-skill-intensive industries."),
 ("p", "These results also bear on where governments should settle refugees and immigrants during mass migration episodes. In Turkey, settling migrants in central rather than non-central regions raises aggregate welfare by an order of magnitude. Existing placement policies weigh job availability and equity across regions, but not the position of host regions in the production network, resulting in forgone welfare gains."),
 ("p", "This mechanism explains why studies comparing host and non-host regions can disagree. Economic migrants tend to settle in large cities, which tend to be more central. There, production networks dampen local wage effects, and spillovers bias comparisons between host and non-host regions in either direction, depending on the economy's technology parameters. Refugees, in contrast, settle close to the border they cross, in typically non-central regions where spillovers are negligible and such comparisons recover the effects of immigration."),
 ("papers", "Related papers", ["pp", "siv", "minwage"]),

 ("banner", "jmp2"),
 ("p", "The policy debate around immigration in the United States (and in many other countries) is whether immigrants “steal” American jobs or bring unique talent that makes the economy more productive. The production network framework helps us answer this question."),
 ("h3", "A new test: cheap labor or better skills?"),
 ("fig", "svg:chains", "Two ways a shock travels through the production network", ""),
 ("p", "When labor and intermediates are gross complements, a pure labor supply shock makes both suppliers and customers better off, while a technology shock makes mainly customers better off and actually hurts suppliers indirectly. Hence, how much more customers benefit compared to suppliers can help us quantify how much productivity gain immigrants bring."),
 ("h3", "Taking the test to H-1B"),
 ("p", "How can we use this intuition to test whether H-1B immigrants increase US productivity? The recent literature on H-1B exploits the visa lottery ([Doran, Gelber, and Isen, 2022](https://doi.org/10.1086/720467); [Mahajan et al., 2024](https://www.richmondfed.org/publications/research/working_papers/2024/wp_24-04)), which creates gold-standard variation for causal identification. However, the lottery does not let us look at input-output spillovers, for two reasons. First, the US does not have data on firm-to-firm transactions like Turkey does (a VAT system has its advantages). Second, which firms get the most H-1B workers changes over time: in the early 2010s, it was mainly Indian IT firms, and in more recent years, it is the tech giants."),
 ("row", [("h1b_top_firms.png", "Top H-1B sponsoring firms by year", ""),
          ("h1b_naics4_weight.png", "Industry-level H-1B shares over time", "")]),
 ("p", "So, what can we do? The empirical intuition is that H-1B is first and foremost an industry policy. Which firms acquire H-1Bs changes over time, but which industries get the most H-1Bs does not: it is essentially a handful of industries that are most exposed."),
 ("p", "The event we use is the relaxation of H-1B quotas between 1999 and 2003, which allowed for 490,000 additional visas during this period. The shock left a handful of industries highly exposed, and in the US we observe the industry-level input-output network, so we can look at forward and backward propagation at the industry level."),
 ("row", [("h1b_cap_history.png", "Statutory H-1B cap", ""),
          ("h1b_scatter_persistence.png", "H-1B exposure vs. skill intensity", "")]),
 ("p", "There is one more challenge: pre-trends. The H-1B cap was relaxed during the dot-com boom: there was an increasing need for particular skills, so Congress raised the visa cap to bring more people in. This is visible in the data. The industries that would eventually be exposed to H-1B workers were already following differential trajectories, resulting in the standard pre-trend problem. To address this, we use the reduced-form version of SIV. For every industry, we find synthetic control weights among industries in the same skill group by matching on the trends in outcomes, build a synthetic industry with these weights, difference it out from the real data, and apply OLS to the differenced data. Because there are few effective clusters, inference is through randomization ([Ferman and Pinto, 2019](https://doi.org/10.1162/rest_a_00759))."),
 ("h3", "Results"),
 ("p", "The gains come from non-STEM occupations. There is no detectable decrease in STEM wages, although we cannot rule out decreases in wages consistent with the theory."),
 ("fig", "s_h1b_forest.png", "The gain is in non-STEM occupations",
  "Pre-existing immigrants gain too: not pure substitution. Short run (solid) and long run (dashed): similar."),
 ("p", "Forward exposure brings large gains, while backward exposure has a null effect. Compare this to the low-skill immigration shock in Turkey, where both forward and backward trading partners benefited."),
 ("fig", "s_h1b_io.png", "Forward propagation is positive, backward is null",
  "Forward: how much an industry buys from directly-exposed industries. Backward: how much it sells to directly-exposed industries."),
 ("p", "We use the model to back out the productivity gain associated with immigration."),
 ("fig", "s_h1b_chi.png", "The inflow carried productivity: χ ≈ 0.4",
  "0.4% Hicks-neutral productivity gain for each pp increase in H-1B immigration. χ = 0.47 (QCEW) and 0.33 (ACS)."),
 ("h3", "Policy"),
 ("p", "Recent policy, including the $100,000 fee on new H-1B petitions ([Bloomberg Law](" + BLOOMBERG_URL + ")), is restricting the program."),
 ("box", "restriction"),
 ("papers", "Related paper", ["canada"]),

 ("section", "refugees", "Refugee Crises"),
 ("p", "My work on immigration began with the refugee crises of the past decade and a question they raised: what are the consequences of granting or denying refugees work permits for the host economy? I study this question in the two largest refugee crises in the world: 3.6 million Syrians in Turkey and 2.5 million Venezuelans in Colombia."),
 ("papers", "", ["colombia", "feoil", "noway"]),

 ("section", "remote", "Remote Work and Gender Inequality"),
 ("p", "My second line of research studies child penalties: the disparate impact of parenthood on women's labor market outcomes relative to men's. In developed countries, these penalties explain much of the gender inequality in the labor market. We do not yet know which occupations they come from, or whether technological changes that make occupations more flexible, such as remote work, can reduce them."),
 ("papers", "", ["cpocc", "wfhcp", "ukfathers", "norms"]),
]

RESTRICTION_TITLE = "What 85,000 fewer H-1B workers a year would cost, every year"
RESTRICTION = [("Labor supply in computer services", "−1.1%"), ("Productivity in computer services", "−0.5%"),
               ("Income of non-STEM native college graduates there", "−1.2%"),
               ("Income in customer industries", "−0.5% (1997 network), −0.7% (2017)"),
               ("Real GDP", "−0.13%, of which −0.07% productivity")]
TAKEAWAY = ("H-1B is not only immigration policy. It is technology policy.",
            "Restricting it is less like shielding workers from cheap labor, and more like slowing a technology the whole economy runs on.")
