# Fernando Siman — OIM 3641 Classwork

Senior at Babson College studying Business Administration. This repo tracks my coursework for OIM 3641 (AI App Development), including LLM API calls, retrieval-augmented generation demos, and Python fundamentals.

## Skills & Tools

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

> More badge options: [markdown-badges](https://github.com/Ileriayo/markdown-badges#markdown-badges)

## Directory Structure

```
.
├── README.md                          # This file
├── 01-llm-call.py                     # Basic Gemini API call example
├── 02-python_concepts.ipynb           # Python fundamentals notebook (exercises)
├── 03-demo_create_llamaindex.py       # Document ingestion → LlamaCloud index
├── 03-demo_llama_retrieval.py         # Retrieval demo against a LlamaIndex
├── 03-demo_llama_gemini_retrieval.py  # Retrieval + Gemini generation demo
├── data/                              # Source documents and datasets used by demos
└── random_integers.txt                # Sample data file
```

As the semester progresses, new exercises and project milestones will be added as additional numbered scripts/notebooks (e.g. `04-...`, `05-...`) or subfolders per assignment.

## Install / Run Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/fersimanh/classwork.git
   cd classwork
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install python-dotenv google-genai llama-cloud-services jupyter
   ```
4. Create a `.env` file in the project root with your own API keys (never commit real keys):
   ```
   GEMINI_API_KEY=your-key-here
   LLAMA_CLOUD_API_KEY=your-key-here
   ```
5. Run a script or open a notebook:
   ```bash
   python 01-llm-call.py
   jupyter notebook 02-python_concepts.ipynb
   ```

## Contact / Connect

- LinkedIn: [linkedin.com/in/fernandosimanh](https://linkedin.com/in/fernandosimanh)
- GitHub: [github.com/fersimanh](https://github.com/fersimanh)
- Email: [fernandosiman2012@gmail.com](mailto:fernandosiman2012@gmail.com)
