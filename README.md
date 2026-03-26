# Academic Metadata Extractor

Pipeline en Python para extraer metadatos bibliográficos de artículos académicos desde arXiv y transformar información semiestructurada en datos estructurados exportables a CSV y JSON.

---

## Descripción del proyecto

Este miniproyecto tiene como objetivo automatizar la recolección y organización de información bibliográfica de artículos académicos. A partir de una consulta temática, el sistema obtiene resultados desde arXiv, extrae campos relevantes, limpia el texto y lo transforma en un formato estructurado que puede ser utilizado para análisis, visualización o almacenamiento.

El proyecto fue diseñado como una demostración práctica de:

- extracción de datos desde una fuente académica
- transformación de datos semiestructurados a estructurados
- limpieza y normalización de texto
- organización de un pipeline en Python
- exportación de resultados en formatos reutilizables

---

## Problema que resuelve

Gran parte de la información académica disponible en la web aparece en formatos semiestructurados: páginas con títulos, autores, resúmenes, fechas y categorías que son legibles para humanos, pero no siempre están listas para análisis computacional directo.

Este proyecto busca resolver ese problema tomando registros académicos y convirtiéndolos en una tabla organizada con campos estandarizados.

---

## Objetivo general

Construir un pipeline en Python que permita consultar artículos académicos, extraer sus metadatos bibliográficos y convertirlos en un conjunto de datos estructurado.

---

## Objetivos específicos

- Consultar artículos académicos a partir de una palabra clave o tema.
- Extraer información relevante como título, autores, fecha, resumen y enlace.
- Limpiar y normalizar los campos textuales.
- Convertir los resultados en una estructura tabular.
- Exportar los datos procesados a archivos CSV y JSON.

---

## Fuente de datos

La fuente utilizada en esta primera versión es **arXiv**, un repositorio abierto de artículos académicos ampliamente usado en áreas como informática, lingüística computacional, matemática y física.

Se eligió arXiv porque:

- ofrece acceso a metadatos de artículos
- permite consultas temáticas
- tiene una estructura adecuada para extracción automática
- facilita la construcción de un proyecto reproducible y claro para portafolio

---

## Tecnologías utilizadas

- **Python**  
- **requests** para realizar consultas HTTP  
- **feedparser** para procesar la respuesta de arXiv  
- **pandas** para estructurar y exportar los datos  
- **re** para limpieza de texto  
- **json** para exportación en formato JSON  

---

## Estructura del proyecto

```bash
academic-metadata-extractor/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── output/
│   ├── articles.csv
│   └── articles.json
│
├── README.md
├── requirements.txt
└── main.py

# Resultados obtenidos de la extracción de la matedata

Se realizó un ejemplo con la búsqueda "computational linguistics", donde se obtuvo el siguiente JSON:

[
    {
        "article_id": "http://arxiv.org/abs/1506.05402v1",
        "title": "Editorial for the First Workshop on Mining Scientific Papers: Computational Linguistics and Bibliometrics",
        "authors": "Iana Atanassova, Marc Bertin, Philipp Mayr",
        "authors_count": 3,
        "published": "2015-06-17T18:03:25Z",
        "summary": "The workshop \"Mining Scientific Papers: Computational Linguistics and Bibliometrics\" (CLBib 2015), co-located with the 15th International Society of Scientometrics and Informetrics Conference (ISSI 2015), brought together researchers in Bibliometrics and Computational Linguistics in order to study the ways Bibliometrics can benefit from large-scale text analytics and sense mining of scientific papers, thus exploring the interdisciplinarity of Bibliometrics and Natural Language Processing (NLP). The goals of the workshop were to answer questions like: How can we enhance author network analysis and Bibliometrics using data obtained by text analytics? What insights can NLP provide on the structure of scientific writing, on citation networks, and on in-text citation analysis? This workshop is the first step to foster the reflection on the interdisciplinarity and the benefits that the two disciplines Bibliometrics and Natural Language Processing can drive from it.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/1506.05402v1",
        "pdf_url": "https://arxiv.org/pdf/1506.05402v1"
    },
    {
        "article_id": "http://arxiv.org/abs/1602.00245v1",
        "title": "Statistical methods for linguistic research: Foundational Ideas - Part II",
        "authors": "Bruno Nicenboim, Shravan Vasishth",
        "authors_count": 2,
        "published": "2016-01-31T13:36:20Z",
        "summary": "We provide an introductory review of Bayesian data analytical methods, with a focus on applications for linguistics, psychology, psycholinguistics, and cognitive science. The empirically oriented researcher will benefit from making Bayesian methods part of their statistical toolkit due to the many advantages of this framework, among them easier interpretation of results relative to research hypotheses, and flexible model specification. We present an informal introduction to the foundational ideas behind Bayesian data analysis, using, as an example, a linear mixed models analysis of data from a typical psycholinguistics experiment. We discuss hypothesis testing using the Bayes factor, and model selection using cross-validation. We close with some examples illustrating the flexibility of model specification in the Bayesian framework. Suggestions for further reading are also provided.",
        "category": "stat.AP",
        "url": "https://arxiv.org/abs/1602.00245v1",
        "pdf_url": "https://arxiv.org/pdf/1602.00245v1"
    },
    {
        "article_id": "http://arxiv.org/abs/1601.01126v2",
        "title": "Statistical methods for linguistic research: Foundational Ideas - Part I",
        "authors": "Shravan Vasishth, Bruno Nicenboim",
        "authors_count": 2,
        "published": "2016-01-06T10:27:38Z",
        "summary": "We present the fundamental ideas underlying statistical hypothesis testing using the frequentist framework. We begin with a simple example that builds up the one-sample t-test from the beginning, explaining important concepts such as the sampling distribution of the sample mean, and the iid assumption. Then we examine the p-value in detail, and discuss several important misconceptions about what a p-value does and does not tell us. This leads to a discussion of Type I, II error and power, and Type S and M error. An important conclusion from this discussion is that one should aim to carry out appropriately powered studies. Next, we discuss two common issues we have encountered in psycholinguistics and linguistics: running experiments until significance is reached, and the \"garden-of-forking-paths\" problem discussed by Gelman and others, whereby the researcher attempts to find statistical significance by analyzing the data in different ways. The best way to use frequentist methods is to run appropriately powered studies, check model assumptions, clearly separate exploratory data analysis from confirmatory hypothesis testing, and always attempt to replicate results.",
        "category": "stat.AP",
        "url": "https://arxiv.org/abs/1601.01126v2",
        "pdf_url": "https://arxiv.org/pdf/1601.01126v2"
    },
    {
        "article_id": "http://arxiv.org/abs/1502.04938v2",
        "title": "A Survey of Word Reordering in Statistical Machine Translation: Computational Models and Language Phenomena",
        "authors": "Arianna Bisazza, Marcello Federico",
        "authors_count": 2,
        "published": "2015-02-17T15:59:09Z",
        "summary": "Word reordering is one of the most difficult aspects of statistical machine translation (SMT), and an important factor of its quality and efficiency. Despite the vast amount of research published to date, the interest of the community in this problem has not decreased, and no single method appears to be strongly dominant across language pairs. Instead, the choice of the optimal approach for a new translation task still seems to be mostly driven by empirical trials. To orientate the reader in this vast and complex research area, we present a comprehensive survey of word reordering viewed as a statistical modeling challenge and as a natural language phenomenon. The survey describes in detail how word reordering is modeled within different string-based and tree-based SMT frameworks and as a stand-alone task, including systematic overviews of the literature in advanced reordering modeling. We then question why some approaches are more successful than others in different language pairs. We argue that, besides measuring the amount of reordering, it is important to understand which kinds of reordering occur in a given language pair. To this end, we conduct a qualitative analysis of word reordering phenomena in a diverse sample of language pairs, based on a large collection of linguistic knowledge. Empirical results in the SMT literature are shown to support the hypothesis that a few linguistic facts can be very useful to anticipate the reordering characteristics of a language pair and to select the SMT framework that best suits them.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/1502.04938v2",
        "pdf_url": "https://arxiv.org/pdf/1502.04938v2"
    },
    {
        "article_id": "http://arxiv.org/abs/2405.05966v5",
        "title": "Natural Language Processing RELIES on Linguistics",
        "authors": "Juri Opitz, Shira Wein, Nathan Schneider",
        "authors_count": 3,
        "published": "2024-05-09T17:59:32Z",
        "summary": "Large Language Models (LLMs) have become capable of generating highly fluent text in certain languages, without modules specially designed to capture grammar or semantic coherence. What does this mean for the future of linguistic expertise in NLP? We highlight several aspects in which NLP (still) relies on linguistics, or where linguistic thinking can illuminate new directions. We argue our case around the acronym RELIES that encapsulates six major facets where linguistics contributes to NLP: Resources, Evaluation, Low-resource settings, Interpretability, Explanation, and the Study of language. This list is not exhaustive, nor is linguistics the main point of reference for every effort under these themes; but at a macro level, these facets highlight the enduring importance of studying machine systems vis-à-vis systems of human language.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/2405.05966v5",
        "pdf_url": "https://arxiv.org/pdf/2405.05966v5"
    },
    {
        "article_id": "http://arxiv.org/abs/1906.09569v1",
        "title": "Systematic improvement of user engagement with academic titles using computational linguistics",
        "authors": "Nim Dvir, Ruti Gafni",
        "authors_count": 2,
        "published": "2019-06-23T09:23:08Z",
        "summary": "This paper describes a novel approach to systematically improve information interactions based solely on its wording. Following an interdisciplinary literature review, we recognized three key attributes of words that drive user engagement: (1) Novelty (2) Familiarity (3) Emotionality. Based on these attributes, we developed a model to systematically improve a given content using computational linguistics, natural language processing (NLP) and text analysis (word frequency, sentiment analysis and lexical substitution). We conducted a pilot study (n=216) in which the model was used to formalize evaluation and optimization of academic titles. A between-group design (A/B testing) was used to compare responses to the original and modified (treatment) titles. Data was collected for selection and evaluation (User Engagement Scale). The pilot results suggest that user engagement with digital information is fostered by, and perhaps dependent upon, the wording being used. They also provide empirical support that engaging content can be systematically evaluated and produced. The preliminary results show that the modified (treatment) titles had significantly higher scores for information use and user engagement (selection and evaluation). We propose that computational linguistics is a useful approach for optimizing information interactions. The empirically based insights can inform the development of digital content strategies, thereby improving the success of information interactions.elop more sophisticated interaction measures.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/1906.09569v1",
        "pdf_url": "https://arxiv.org/pdf/1906.09569v1"
    },
    {
        "article_id": "http://arxiv.org/abs/1707.04546v1",
        "title": "Linguistic Markers of Influence in Informal Interactions",
        "authors": "Shrimai Prabhumoye, Samridhi Choudhary, Evangelia Spiliopoulou, Christopher Bogart, Carolyn Penstein Rose, Alan W Black",
        "authors_count": 6,
        "published": "2017-07-14T15:43:45Z",
        "summary": "There has been a long standing interest in understanding `Social Influence' both in Social Sciences and in Computational Linguistics. In this paper, we present a novel approach to study and measure interpersonal influence in daily interactions. Motivated by the basic principles of influence, we attempt to identify indicative linguistic features of the posts in an online knitting community. We present the scheme used to operationalize and label the posts with indicator features. Experiments with the identified features show an improvement in the classification accuracy of influence by 3.15%. Our results illustrate the important correlation between the characteristics of the language and its potential to influence others.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/1707.04546v1",
        "pdf_url": "https://arxiv.org/pdf/1707.04546v1"
    },
    {
        "article_id": "http://arxiv.org/abs/1808.06696v4",
        "title": "Watset: Local-Global Graph Clustering with Applications in Sense and Frame Induction",
        "authors": "Dmitry Ustalov, Alexander Panchenko, Chris Biemann, Simone Paolo Ponzetto",
        "authors_count": 4,
        "published": "2018-08-20T21:06:01Z",
        "summary": "We present a detailed theoretical and computational analysis of the Watset meta-algorithm for fuzzy graph clustering, which has been found to be widely applicable in a variety of domains. This algorithm creates an intermediate representation of the input graph that reflects the \"ambiguity\" of its nodes. Then, it uses hard clustering to discover clusters in this \"disambiguated\" intermediate graph. After outlining the approach and analyzing its computational complexity, we demonstrate that Watset shows competitive results in three applications: unsupervised synset induction from a synonymy graph, unsupervised semantic frame induction from dependency triples, and unsupervised semantic class induction from a distributional thesaurus. Our algorithm is generic and can be also applied to other networks of linguistic data.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/1808.06696v4",
        "pdf_url": "https://arxiv.org/pdf/1808.06696v4"
    },
    {
        "article_id": "http://arxiv.org/abs/1912.11717v3",
        "title": "Adjoint computations by algorithmic differentiation of a parallel solver for time-dependent PDEs",
        "authors": "J. I. Cardesa, L. Hascoët, C. Airiau",
        "authors_count": 3,
        "published": "2019-12-25T21:17:56Z",
        "summary": "A computational fluid dynamics code is differentiated using algorithmic differentiation (AD) in both tangent and adjoint modes. The two novelties of the present approach are 1) the adjoint code is obtained by letting the AD tool Tapenade invert the complete layer of message passing interface (MPI) communications, and 2) the adjoint code integrates time-dependent, non-linear and dissipative (hence physically irreversible) PDEs with an explicit time integration loop running for ca. $10^{6}$ time steps. The approach relies on using the Adjoinable MPI library to reverse the non-blocking communication patterns in the original code, and by controlling the memory overhead induced by the time-stepping loop with binomial checkpointing. A description of the necessary code modifications is provided along with the validation of the computed derivatives and a performance comparison of the tangent and adjoint codes.",
        "category": "physics.comp-ph",
        "url": "https://arxiv.org/abs/1912.11717v3",
        "pdf_url": "https://arxiv.org/pdf/1912.11717v3"
    },
    {
        "article_id": "http://arxiv.org/abs/2503.19260v1",
        "title": "Linguistic Blind Spots of Large Language Models",
        "authors": "Jiali Cheng, Hadi Amiri",
        "authors_count": 2,
        "published": "2025-03-25T01:47:13Z",
        "summary": "Large language models (LLMs) are the foundation of many AI applications today. However, despite their remarkable proficiency in generating coherent text, questions linger regarding their ability to perform fine-grained linguistic annotation tasks, such as detecting nouns or verbs, or identifying more complex syntactic structures like clauses in input texts. These tasks require precise syntactic and semantic understanding of input text, and when LLMs underperform on specific linguistic structures, it raises concerns about their reliability for detailed linguistic analysis and whether their (even correct) outputs truly reflect an understanding of the inputs. In this paper, we empirically study the performance of recent LLMs on fine-grained linguistic annotation tasks. Through a series of experiments, we find that recent LLMs show limited efficacy in addressing linguistic queries and often struggle with linguistically complex inputs. We show that the most capable LLM (Llama3-70b) makes notable errors in detecting linguistic structures, such as misidentifying embedded clauses, failing to recognize verb phrases, and confusing complex nominals with clauses. Our results provide insights to inform future advancements in LLM design and development.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/2503.19260v1",
        "pdf_url": "https://arxiv.org/pdf/2503.19260v1"
    },
    {
        "article_id": "http://arxiv.org/abs/1803.09103v1",
        "title": "Machine Learning and Applied Linguistics",
        "authors": "Sowmya Vajjala",
        "authors_count": 1,
        "published": "2018-03-24T13:08:56Z",
        "summary": "This entry introduces the topic of machine learning and provides an overview of its relevance for applied linguistics and language learning. The discussion will focus on giving an introduction to the methods and applications of machine learning in applied linguistics, and will provide references for further study.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/1803.09103v1",
        "pdf_url": "https://arxiv.org/pdf/1803.09103v1"
    },
    {
        "article_id": "http://arxiv.org/abs/2412.15772v1",
        "title": "Linguistic Features Extracted by GPT-4 Improve Alzheimer's Disease Detection based on Spontaneous Speech",
        "authors": "Jonathan Heitz, Gerold Schneider, Nicolas Langer",
        "authors_count": 3,
        "published": "2024-12-20T10:43:42Z",
        "summary": "Alzheimer's Disease (AD) is a significant and growing public health concern. Investigating alterations in speech and language patterns offers a promising path towards cost-effective and non-invasive early detection of AD on a large scale. Large language models (LLMs), such as GPT, have enabled powerful new possibilities for semantic text analysis. In this study, we leverage GPT-4 to extract five semantic features from transcripts of spontaneous patient speech. The features capture known symptoms of AD, but they are difficult to quantify effectively using traditional methods of computational linguistics. We demonstrate the clinical significance of these features and further validate one of them (\"Word-Finding Difficulties\") against a proxy measure and human raters. When combined with established linguistic features and a Random Forest classifier, the GPT-derived features significantly improve the detection of AD. Our approach proves effective for both manually transcribed and automatically generated transcripts, representing a novel and impactful use of recent advancements in LLMs for AD speech analysis.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/2412.15772v1",
        "pdf_url": "https://arxiv.org/pdf/2412.15772v1"
    },
    {
        "article_id": "http://arxiv.org/abs/2005.12543v3",
        "title": "Computing persistent Stiefel-Whitney classes of line bundles",
        "authors": "Raphaël Tinarrage",
        "authors_count": 1,
        "published": "2020-05-26T06:56:58Z",
        "summary": "We propose a definition of persistent Stiefel-Whitney classes of vector bundle filtrations. It relies on seeing vector bundles as subsets of some Euclidean spaces. The usual Čech filtration of such a subset can be endowed with a vector bundle structure, that we call a Čech bundle filtration. We show that this construction is stable and consistent. When the dataset is a finite sample of a line bundle, we implement an effective algorithm to compute its persistent Stiefel-Whitney classes. In order to use simplicial approximation techniques in practice, we develop a notion of weak simplicial approximation. As a theoretical example, we give an in-depth study of the normal bundle of the circle, which reduces to understanding the persistent cohomology of the torus knot (1,2). We illustrate our method on several datasets inspired by image analysis.",
        "category": "math.AT",
        "url": "https://arxiv.org/abs/2005.12543v3",
        "pdf_url": "https://arxiv.org/pdf/2005.12543v3"
    },
    {
        "article_id": "http://arxiv.org/abs/2309.04919v2",
        "title": "The Emergence of Chunking Structures with Hierarchical RNN",
        "authors": "Zijun Wu, Anup Anand Deshmukh, Yongkang Wu, Jimmy Lin, Lili Mou",
        "authors_count": 5,
        "published": "2023-09-10T02:55:12Z",
        "summary": "In Natural Language Processing (NLP), predicting linguistic structures, such as parsing and chunking, has mostly relied on manual annotations of syntactic structures. This paper introduces an unsupervised approach to chunking, a syntactic task that involves grouping words in a non-hierarchical manner. We present a Hierarchical Recurrent Neural Network (HRNN) designed to model word-to-chunk and chunk-to-sentence compositions. Our approach involves a two-stage training process: pretraining with an unsupervised parser and finetuning on downstream NLP tasks. Experiments on multiple datasets reveal a notable improvement of unsupervised chunking performance in both pretraining and finetuning stages. Interestingly, we observe that the emergence of the chunking structure is transient during the neural model's downstream-task training. This study contributes to the advancement of unsupervised syntactic structure discovery and opens avenues for further research in linguistic theory.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/2309.04919v2",
        "pdf_url": "https://arxiv.org/pdf/2309.04919v2"
    },
    {
        "article_id": "http://arxiv.org/abs/1911.00317v1",
        "title": "On the Linguistic Representational Power of Neural Machine Translation Models",
        "authors": "Yonatan Belinkov, Nadir Durrani, Fahim Dalvi, Hassan Sajjad, James Glass",
        "authors_count": 5,
        "published": "2019-11-01T12:13:45Z",
        "summary": "Despite the recent success of deep neural networks in natural language processing (NLP), their interpretability remains a challenge. We analyze the representations learned by neural machine translation models at various levels of granularity and evaluate their quality through relevant extrinsic properties. In particular, we seek answers to the following questions: (i) How accurately is word-structure captured within the learned representations, an important aspect in translating morphologically-rich languages? (ii) Do the representations capture long-range dependencies, and effectively handle syntactically divergent languages? (iii) Do the representations capture lexical semantics? We conduct a thorough investigation along several parameters: (i) Which layers in the architecture capture each of these linguistic phenomena; (ii) How does the choice of translation unit (word, character, or subword unit) impact the linguistic properties captured by the underlying representations? (iii) Do the encoder and decoder learn differently and independently? (iv) Do the representations learned by multilingual NMT models capture the same amount of linguistic information as their bilingual counterparts? Our data-driven, quantitative evaluation illuminates important aspects in NMT models and their ability to capture various linguistic phenomena. We show that deep NMT models learn a non-trivial amount of linguistic information. Notable findings include: i) Word morphology and part-of-speech information are captured at the lower layers of the model; (ii) In contrast, lexical semantics or non-local syntactic and semantic dependencies are better represented at the higher layers; (iii) Representations learned using characters are more informed about wordmorphology compared to those learned using subword units; and (iv) Representations learned by multilingual models are richer compared to bilingual models.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/1911.00317v1",
        "pdf_url": "https://arxiv.org/pdf/1911.00317v1"
    },
    {
        "article_id": "http://arxiv.org/abs/1707.03765v3",
        "title": "Computing Singularly Perturbed Differential Equations",
        "authors": "Sabyasachi Chatterjee, Amit Acharya, Zvi Artstein",
        "authors_count": 3,
        "published": "2017-07-06T19:58:50Z",
        "summary": "A computational tool for coarse-graining nonlinear systems of ordinary differential equations in time is discussed. Three illustrative model examples are worked out that demonstrate the range of capability of the method. This includes the averaging of Hamiltonian as well as dissipative microscopic dynamics whose `slow' variables, defined in a precise sense, can often display mixed slow-fast response as in relaxation oscillations, and dependence on initial conditions of the fast variables. Also covered is the case where the quasi-static assumption in solid mechanics is violated. The computational tool is demonstrated to capture all of these behaviors in an accurate and robust manner, with significant savings in time. A practically useful strategy for initializing short bursts of microscopic runs for the accurate computation of the evolution of slow variables is also developed.",
        "category": "math.NA",
        "url": "https://arxiv.org/abs/1707.03765v3",
        "pdf_url": "https://arxiv.org/pdf/1707.03765v3"
    },
    {
        "article_id": "http://arxiv.org/abs/2503.11302v4",
        "title": "Are formal and functional linguistic mechanisms dissociated in language models?",
        "authors": "Michael Hanna, Yonatan Belinkov, Sandro Pezzelle",
        "authors_count": 3,
        "published": "2025-03-14T11:11:03Z",
        "summary": "Although large language models (LLMs) are increasingly capable, these capabilities are unevenly distributed: they excel at formal linguistic tasks, such as producing fluent, grammatical text, but struggle more with functional linguistic tasks like reasoning and consistent fact retrieval. Inspired by neuroscience, recent work suggests that to succeed on both formal and functional linguistic tasks, LLMs should use different mechanisms for each; such localization could either be built-in or emerge spontaneously through training. In this paper, we ask: do current models, with fast-improving functional linguistic abilities, exhibit distinct localization of formal and functional linguistic mechanisms? We answer this by finding and comparing the \"circuits\", or minimal computational subgraphs, responsible for various formal and functional tasks. Comparing 5 LLMs across 10 distinct tasks, we find that while there is indeed little overlap between circuits for formal and functional tasks, there is also little overlap between formal linguistic tasks, as exists in the human brain. Thus, a single formal linguistic network, unified and distinct from functional task circuits, remains elusive. However, in terms of cross-task faithfulness - the ability of one circuit to solve another's task - we observe a separation between formal and functional mechanisms, suggesting that shared mechanisms between formal tasks may exist.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/2503.11302v4",
        "pdf_url": "https://arxiv.org/pdf/2503.11302v4"
    },
    {
        "article_id": "http://arxiv.org/abs/1109.6113v1",
        "title": "Improved multiscale computational strategies for delamination",
        "authors": "Olivier Allix, Pierre Gosselet, Pierre Kerfriden",
        "authors_count": 3,
        "published": "2011-09-28T06:53:00Z",
        "summary": "This paper presents a three-scale computational strategy for the study of composite modeled at the mesoscale so that delamination can be reliably simulated. The solver is based on a LaTIn approach so that nonlinearities can be tackled at the local scale. We show how search directions which are parameters of the method need to be updated according to the delamination status of interfaces. We also present the parallelization of the macro problem which transmits long-range phenomena and warranty the scalabilty of the method; this parallelization is based on the balancing domain decomposition method, it leads to the introduction of a third (super-macro) scale.",
        "category": "physics.comp-ph",
        "url": "https://arxiv.org/abs/1109.6113v1",
        "pdf_url": "https://arxiv.org/pdf/1109.6113v1"
    },
    {
        "article_id": "http://arxiv.org/abs/2010.12107v1",
        "title": "Accelerating computational modeling and design of high-entropy alloys",
        "authors": "Rahul Singh, Aayush Sharma, Prashant Singh, Ganesh Balasubramanian, Duane D. Johnson",
        "authors_count": 5,
        "published": "2020-10-22T23:19:28Z",
        "summary": "With huge design spaces for unique chemical and mechanical properties, we remove a roadblock to computational design of {high-entropy alloys} using a metaheuristic hybrid Cuckoo Search (CS) for \"on-the-fly\" construction of Super-Cell Random APproximates (SCRAPs) having targeted atomic site and pair probabilities on arbitrary crystal lattices. Our hybrid-CS schema overcomes large, discrete combinatorial optimization by ultrafast global solutions that scale linearly in system size and strongly in parallel, e.g. a 4-element, 128-atom model [a $10^{73+}$ space] is found in seconds -- a reduction of 13,000+ over current strategies. With model-generation eliminated as a bottleneck, computational alloy design can be performed that is currently impossible or impractical. We showcase the method for real alloys with varying short-range order. Being problem-agnostic, our hybrid-CS schema offers numerous applications in diverse fields.",
        "category": "cond-mat.mtrl-sci",
        "url": "https://arxiv.org/abs/2010.12107v1",
        "pdf_url": "https://arxiv.org/pdf/2010.12107v1"
    },
    {
        "article_id": "http://arxiv.org/abs/1809.04179v2",
        "title": "What can linguistics and deep learning contribute to each other?",
        "authors": "Tal Linzen",
        "authors_count": 1,
        "published": "2018-09-11T21:55:11Z",
        "summary": "Joe Pater's target article calls for greater interaction between neural network research and linguistics. I expand on this call and show how such interaction can benefit both fields. Linguists can contribute to research on neural networks for language technologies by clearly delineating the linguistic capabilities that can be expected of such systems, and by constructing controlled experimental paradigms that can determine whether those desiderata have been met. In the other direction, neural networks can benefit the scientific study of language by providing infrastructure for modeling human sentence processing and for evaluating the necessity of particular innate constraints on language acquisition.",
        "category": "cs.CL",
        "url": "https://arxiv.org/abs/1809.04179v2",
        "pdf_url": "https://arxiv.org/pdf/1809.04179v2"
    }
]
