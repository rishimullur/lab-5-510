Lab 5

# AI Resume Coach

This is a simple streamlit app that utilizes the Gemini API and Streamlit to act as an AI resume helper.

## Installation

1. Clone the repository:

    ```shell
    git clone git@github.com:rishimullur/lab-5-510.git
    ```

2. Navigate to the project directory:

    ```shell
    cd lab-5-510
    ```

3. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

## Usage

1. Set up your Gemini API credentials by creating a `.env` file in the project directory and adding the following lines:

    ```shell
    GEMINI_API_KEY="your-api-key"
    ```

2. Run the app:

    ```shell
    streamlit run app.py
    ```

3. Open your web browser and go to `http://localhost:8501` to access the app.


# Prompt Improvements

Some common problems faced when developing LLM-powered apps include:

a. Ensuring the prompts are clear, concise, and unambiguous to elicit the desired response from the language model.
b. Handling edge cases, such as ambiguous or nonsensical inputs, where the language model may struggle to provide a meaningful response.
c. Maintaining consistency and coherence in the language model's responses, especially for longer or more complex prompts.
d. Tailoring the language model's tone, personality, and level of detail to match the intended use case and target audience.

Many of these problems can be mitigated or addressed through the use of advanced prompting techniques, such as:

a. Chain of Thought Prompting: This technique encourages the language model to break down complex tasks into a series of steps, making it easier to follow its thought process and provide more coherent and reliable responses.
b. Persona Prompting: By specifying a persona or character for the language model to assume, you can better control the tone, level of detail, and overall style of its responses.
c. Context Injections: Providing additional context or instructions within the prompt can help guide the language model's responses and ensure they are tailored to the specific use case.
d. Prompt Debugging: Techniques like prompt echoing, where the language model restates the prompt in its own words, can help identify ambiguities or misunderstandings in the prompt before generating a response.

The new prompting techniques can address the problems faced in previous LLM-powered app development in the following ways:

a. Clear and unambiguous prompts: By using techniques like persona prompting and context injections, you can ensure that the prompts are more specific and tailored to the app's requirements, reducing the likelihood of ambiguous or undesirable responses.
b. Handling edge cases: Chain of thought prompting can help the language model break down complex or edge-case scenarios into a series of logical steps, making it easier to reason about and provide more reliable responses.
c. Improved consistency and coherence: The combination of chain of thought prompting, persona prompting, and context injections can help maintain consistency and coherence in the language model's responses, even for longer or more complex prompts.
d. Tailored tone and level of detail: By defining a clear persona for the language model to assume, you can better control the tone, personality, and level of detail in its responses, ensuring they align with the app's intended use case and target audience.
