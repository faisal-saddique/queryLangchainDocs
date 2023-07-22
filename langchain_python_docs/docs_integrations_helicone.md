Helicone
========

This page covers how to use the [Helicone](https://helicone.ai) ecosystem within LangChain.

What is Helicone?[​](#what-is-helicone "Direct link to What is Helicone?")
--------------------------------------------------------------------------

Helicone is an [open source](https://github.com/Helicone/helicone) observability platform that proxies your OpenAI traffic and provides you key insights into your spend, latency and usage.

![Helicone](/assets/images/HeliconeDashboard-bc06f9888dbb03ff98d894fe9bec2b29.png)

Quick start[​](#quick-start "Direct link to Quick start")
---------------------------------------------------------

With your LangChain environment you can just add the following parameter.

    export OPENAI_API_BASE="https://oai.hconeai.com/v1"

Now head over to [helicone.ai](https://helicone.ai/onboarding?step=2) to create your account, and add your OpenAI API key within our dashboard to view your logs.

![Helicone](/assets/images/HeliconeKeys-9ff580101e3a63ee05e2fa67b8def03c.png)

How to enable Helicone caching[​](#how-to-enable-helicone-caching "Direct link to How to enable Helicone caching")
------------------------------------------------------------------------------------------------------------------

    from langchain.llms import OpenAIimport openaiopenai.api_base = "https://oai.hconeai.com/v1"llm = OpenAI(temperature=0.9, headers={"Helicone-Cache-Enabled": "true"})text = "What is a helicone?"print(llm(text))

[Helicone caching docs](https://docs.helicone.ai/advanced-usage/caching)

How to use Helicone custom properties[​](#how-to-use-helicone-custom-properties "Direct link to How to use Helicone custom properties")
---------------------------------------------------------------------------------------------------------------------------------------

    from langchain.llms import OpenAIimport openaiopenai.api_base = "https://oai.hconeai.com/v1"llm = OpenAI(temperature=0.9, headers={        "Helicone-Property-Session": "24",        "Helicone-Property-Conversation": "support_issue_2",        "Helicone-Property-App": "mobile",      })text = "What is a helicone?"print(llm(text))

[Helicone property docs](https://docs.helicone.ai/advanced-usage/custom-properties)