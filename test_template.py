from langchain_core.example_selectors import LengthBasedExampleSelector
from langchain_core.prompts  import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from jinja2 import Environment, FileSystemLoader



def load_template_1():
    template = """写一个PromptTemplate 用于{domain}的数据生成"""

    prompt = PromptTemplate(input_variables=["domain"], template=template)

    print(prompt.format(domain="Education"))
    print(prompt.format_prompt(domain="Education").to_messages())


def load_template_2():
    template_path = r"./single_turn.jinja2"
    prompt_from_file = PromptTemplate.from_file(template_path, encoding="utf-8")
    print(prompt_from_file.format(domain="LangChain", solt="xx"))


def load_few_shot():
    # 定义示例
    examples = [
        {"title": "今日份的小确幸", "content": "早上的一杯咖啡。"},
        {"title": "一个人的西藏", "content": "独自一人踏上西藏之旅，每一步都是风景，每一刻都是故事。这里的蓝天白云，让我忘记了世界的喧嚣。"},
        {"title": "夏日防晒必备良品", "content": "分享我这个夏天最爱的防晒霜，轻薄不油腻，让我在炎炎夏日也能享受阳光而不畏惧。"}
    ]
    # 创建示例模版
    example_prompt = PromptTemplate(
        input_variables=["title", "content"], template="标题: {title}\n内容：{content}"
    )

    example_selector = LengthBasedExampleSelector(
        examples=examples,
        example_prompt=example_prompt,
        max_length=5,
    )

    dynamic_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix="根据文案写总结",
        suffix="创作个{title}：",
        input_variables=["title"],
    )

    # print(example_prompt.format(**examples[0]))
    # 创建 FewShotPromptTemplate
    # fewShotprompt = FewShotPromptTemplate(
    #     examples=examples,
    #     example_prompt=example_prompt,
    #     example_separator="\n\n",
    #     prefix="想要创作出具有小红书风格的内容，请参考以下示例：",
    #     suffix="根据上述示例，尝试创作一个{user_input}。",
    #     input_variables=["user_input"]
    # )
    # 生成提示
    print(dynamic_prompt.format(title="新的故事"))


def load_jinjia2():
    jinjia2_path = "./single_turn.jinja2"
    prompt_from_file = PromptTemplate.from_file(jinjia2_path, encoding="utf-8")
    print(prompt_from_file.format(domain="LangChain", solt="xx"))


def load_jinja2_template():
    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template("sys_msg_template_example.jinja2")
    args = {'assistant_expertise': "helpful"}
    SYS_MSG_ASSISTANT = template.render(**args)
    print(SYS_MSG_ASSISTANT)


import sys
# sys.path.append("../")

from prompts.prompt_manager import PromptManager

def load_prompt_manager():
    support_prompt = PromptManager.get_prompt(
        "ticket_analysis", pipeline='support', v_b2="xxxxxxxxxxxx", name="Bob", ref_entities=None, gen_requirements=['要求1', '要求2'], shot_num=3, intent_scene="XX", ticket={"movie": 'Adam'},
    )

    helpdesk_prompt = PromptManager.get_template_info(
        "ticket_analysis"
    )

    print(support_prompt)
    print("-*"*10)

    print(helpdesk_prompt)

    # messages = []
    # sys_template = {"role": "system", "content": support_prompt}
    #
    # print(type(sys_template))
    # print(sys_template)
    # print(helpdesk_prompt)

def main():
    # load_template_1()
    # load_template_2()
    # load_few_shot()
    # load_jinjia2()
    # load_jinja2_template()
    load_prompt_manager()



if __name__ == "__main__":
    main()
