# CRISPR-GPT: LLM Agents for Automated Gene-Editing
<p align="center">
<img width="600" alt="image" src="https://github.com/user-attachments/assets/701e7878-1f37-4dd1-a256-b68141a549fc">
</p>
CRISPR-GPT is an innovative Large Language Model (LLM) agent designed to automate and streamline the process of designing gene-editing experiments. By leveraging the power of advanced language models, CRISPR-GPT assists researchers in planning, executing, and analyzing CRISPR-based gene editing tasks with unprecedented efficiency and accuracy.

## CRISPR-GPT Architecture

<img width="830" alt="image" src="https://github.com/user-attachments/assets/56f830b8-a434-4fba-b9c4-ea54e0495f15">

The backbone of CRISPR-GPT involves multi-agent collaboration between four core components: 

(1) **LLM Planner Agent** is responsible for configuring tasks, it automatically performs task decomposition and planning based on the user’s request.

(2) **Task Executor Agent** implements the chain of state machines from the Planner Agent, and is responsible for providing instructions, feedback, receiving input from User-Proxy Agent, and calling Tool Provider agent.

(3) **LLM User-Proxy Agent** is responsible for interacting with the Task Executor on behalf of the user, where the user can monitor the process and provide corrections to the User-Proxy Agent.

(4) **Tool Providers** support diverse external tools and connect to search engines or databases via API calls.


## CRISPR-GPT Supports 4 Gene-editing Scenarios with 3 User Modes

<img width="830" alt="image" src="https://github.com/user-attachments/assets/401a6223-cddb-4f74-a369-77e34fdfbe7a">

CRISPR-GPT supports four primary gene-editing modalities: **knockout**, **base-editing**, **prime-editing**, **epigenetic editing**, and offers three user interaction modes:

(1) **Meta mode**: Step-by-Step Guidance on Pre-defined Gene-editing Meta-Tasks

(2) **Auto mode**: Customized Guidance on Free-style User Requests

(3) **QA mode**: Real-time Answers on Ad Hoc Questions

## Demo

We have built a demo website with online version of CRISPR-GPT fully deployed:
https://www.crispr-gpt.com/

Please sign up for early access and beta testing at:
https://forms.gle/QBgEuJv5aEbGnmTe7

**Demo Video 1: Multi-target Cas12a editing of TGFBR1 in A549 lung cancer cells**
- Automated Cas12a gRNA design with exon suggestion, delivery method selection for A549 cells.
- Detailed protocol provided for cloning, viral packaging, editing validation.
- Automated validation primer design (Primer3) and NGS data analysis (CRISPResso2 by Pinello Lab)
<video width="600" controls>
  <source src="https://github.com/user-attachments/assets/ba907f73-38ba-4394-a530-bddceea07bcc" type="video/quicktime">
  Your browser does not support the video tag.
</video>

**Demo Video 2: Targeting APOE at user-defined ClinVar variant locus in primary human hepatocyte**
- Automated gRNA design directly targeting user-defined locus near ClinVar variant.
- Delivery method suggestion and predicting off-target effect (CRISPRitz by Pinello Lab)
<video width="600" controls>
  <source src="https://github.com/user-attachments/assets/411e45f8-5b99-4a75-88fd-b3c729b0b1a6" type="video/quicktime">
  Your browser does not support the video tag.
</video>

**Demo Video 3: Maximizing Loss-of-function success and minimizing Off-target when editing human BRD4**
- Automated gRNA design with exon suggestion to target BRD4 key fucntional domain, maximizing success probability.
- Predicting off-target effect of selected gRNA (CRISPRitz by Pinello Lab)
<video width="600" controls>
  <source src="https://github.com/user-attachments/assets/a7fb04b4-70d1-4a91-a655-e34d5503cc80" type="video/quicktime">
  Your browser does not support the video tag.
</video>

The demo above illustrates the step-by-step interaction between the user and the CRISPR-GPT agent, highlighting its ability to provide expert-level assistance in real-time and automate multiple key tasks (detailed below).

## CRISPR-GPT Supports 22 Unqiue Gene-editing Tasks

<img width="830" alt="image" src="https://github.com/user-attachments/assets/6e486915-c9cc-43af-b855-f12734414b69">

<!--
## Getting Started

### Installation

To get started with CRISPR-GPT, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/crispr-gpt.git
   ```

2. Navigate to the project directory:
   ```
   cd crispr-gpt
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Run the main application:
   ```
   python main.py
   ```

2. Follow the on-screen prompts to interact with the CRISPR-GPT agent.

For more detailed instructions and advanced usage, please refer to our [README](README.md) file.
-->
## Roadmap

We are committed to continuously improving CRISPR-GPT and expanding its capabilities. Our roadmap includes:



- **Support for New CRISPR Methods and Workflows**: examples include Cas13-based RNA-editing.
- **Improved LLM via User/Expert Feedback**: Enhancing AI performance through fine-tuning with larger datasets, your expertise and feedback needed so please sign up for testing CRISPR-GPT as noted above.
- **User Interface Upgrades**: Creating a more intuitive and customizable front end for managing experiments.
- **Integration with Lab Automation**: Facilitating hands-on execution of experiments using robotics and lab automation tools.
- **Integration with Lab Notebook**: Developing APIs for integration with existing laboratory information management systems (LIMS).

We value user feedback and will be actively incorporating suggestions from the research community to make CRISPR-GPT an indispensable tool in gene editing research.
<!--
## Prerequisites

To use CRISPR-GPT, you'll need:

- Python 3.7 or higher
- OpenAI API key (for LLM interactions)
- Gradio (for front-end interface if you'd like to test locally)
- Required Python libraries (install via pip install -r requirements.txt)
-->
## Citation

If you use CRISPR-GPT in your research, please cite our work:

```
Qu, Y.*, Huang, K-X.*, et al. CRISPR-GPT: An LLM Agent for Automated Design of Gene-Editing Experiments. 2024.04.25.591003 Preprint at https://doi.org/10.1101/2024.04.25.591003 (2024). * Equal contribution.
```

## Contact

For questions, suggestions, or collaborations, please contact:

[CRISPR-GPT Team] Emails: 

Le Cong: [congle@stanford.edu]
Yuanhao Qu: [yhqu@stanford.edu]
Kaixuan Huang: [kaixuanh@princeton.edu]
Mengdi Wang: [mengdiw@princeton.edu]

---
