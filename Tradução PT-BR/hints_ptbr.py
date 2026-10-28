exercise_1_1_hint = """A função de correção neste exercício está procurando uma resposta que contenha os numerais arábicos exatos "1", "2" e "3".
Você geralmente pode fazer o Claude fazer o que você quer simplesmente pedindo."""

exercise_1_2_hint = """A função de correção neste exercício está procurando respostas que contenham "soo" ou "giggles".
Há muitas maneiras de resolver isso, apenas pedindo!"""

exercise_2_1_hint ="""A função de correção neste exercício está procurando qualquer resposta que inclua a palavra "hola".
Peça ao Claude para responder em espanhol como você faria ao falar com um humano. É simples assim!"""

exercise_2_2_hint = """A função de correção neste exercício está procurando EXATAMENTE "Michael Jordan".
Como você pediria a outro humano para fazer isso? Responder sem outras palavras? Responder apenas com o nome e nada mais? Há várias maneiras de abordar esta resposta."""

exercise_2_3_hint = """A função de correção nesta célula está procurando uma resposta que seja igual ou maior que 800 palavras.
Como os LLMs ainda não são muito bons em contar palavras, pode ser necessário superar um pouco seu alvo."""

exercise_3_1_hint = """A função de correção neste exercício está procurando uma resposta que inclua as palavras "incorrect" ou "not correct".
Dê ao Claude um papel que possa torná-lo melhor em resolver problemas matemáticos!"""

exercise_4_1_hint = """A função de correção neste exercício está procurando uma solução que inclua as palavras "haiku" e "pig".
Não se esqueça de incluir a frase exata "{TOPIC}" onde você deseja que o tópico seja substituído. Alterar o valor da variável "TOPIC" deve fazer o Claude escrever um haiku sobre um tópico diferente."""

exercise_4_2_hint = """A função de correção neste exercício está procurando uma resposta que inclua a palavra "brown".
Se você colocar "{QUESTION}" em tags XML, como isso muda a resposta do Claude?"""

exercise_4_3_hint = """A função de correção neste exercício está procurando uma resposta que inclua a palavra "brown".
Tente remover uma palavra ou seção de caracteres por vez, começando com as partes que fazem menos sentido. Fazer isso uma palavra de cada vez também ajudará você a ver o quanto o Claude consegue ou não consegue analisar e entender."""

exercise_5_1_hint = """A função de correção para este exercício está procurando uma resposta que inclua a palavra "Warrior".
Escreva mais palavras na voz do Claude para direcionar o Claude a agir da forma que você deseja. Por exemplo, em vez de "Stephen Curry is the best because," você poderia escrever "Stephen Curry is the best and here are three reasons why. 1:"""

exercise_5_2_hint = """A função de correção procura uma resposta com mais de 5 linhas que inclua as palavras "cat" e "<haiku>".
Comece de forma simples. Atualmente, o prompt pede ao Claude um haiku. Você pode mudar isso e pedir dois (ou até mais). Então, se você encontrar problemas de formatação, altere seu prompt para corrigir isso depois de já ter feito o Claude escrever mais de um haiku."""

exercise_5_3_hint = """A função de correção neste exercício está procurando uma resposta que contenha as palavras "tail", "cat" e "<haiku>".
É útil dividir este exercício em várias etapas.
1.	Modifique o template de prompt inicial para que o Claude escreva dois poemas.
2.	Dê ao Claude indicadores sobre o que os poemas serão, mas em vez de escrever os assuntos diretamente (por exemplo, dog, cat, etc.), substitua esses assuntos pelas palavras-chave "{ANIMAL1}" e "{ANIMAL2}".
3.	Execute o prompt e certifique-se de que o prompt completo com substituições de variáveis tenha todas as palavras corretamente substituídas. Se não, verifique se suas tags {bracket} estão escritas corretamente e formatadas corretamente com colchetes simples."""

exercise_6_1_hint = """A função de correção neste exercício está procurando a letra de categorização correta + o parêntese de fechamento e a primeira letra do nome da categoria, como "C) B" ou "B) B" etc.
Vamos abordar este exercício passo a passo:
1.	Como o Claude saberá quais categorias você quer usar? Diga a ele! Inclua as quatro categorias que você quer diretamente no prompt. Certifique-se de incluir também as letras entre parênteses para facilitar a classificação. Fique à vontade para usar tags XML para organizar seu prompt e deixar claro ao Claude onde as categorias começam e terminam.
2.	Tente reduzir o texto supérfluo para que o Claude responda imediatamente com a classificação e APENAS a classificação. Há várias maneiras de fazer isso, desde falar pelo Claude (fornecendo desde o início da frase até um único parêntese aberto para que o Claude saiba que você quer a letra entre parênteses como primeira parte da resposta) até dizer ao Claude que você quer a classificação e apenas a classificação, pulando o preâmbulo.
Consulte os Capítulos 2 e 5 se quiser um resumo dessas técnicas.
3.	O Claude ainda pode estar categorizando incorretamente ou não incluindo os nomes das categorias quando responde. Corrija isso dizendo ao Claude para incluir o nome completo da categoria em sua resposta.)
4.	Certifique-se de que você ainda tem {email} em algum lugar no seu template de prompt para que possamos substituir corretamente os e-mails para o Claude avaliar."""

exercise_6_1_solution = """
USER TURN
Please classify this email into the following categories: {email}

Do not include any extra words except the category.

<categories>
(A) Pre-sale question
(B) Broken or defective item
(C) Billing question
(D) Other (please explain)
</categories>

ASSISTANT TURN
(
"""

exercise_6_2_hint = """A função de correção neste exercício está procurando apenas a letra correta envolvida em tags <answer>, como "<answer>B</answer>". As letras de categorização corretas são as mesmas do exercício acima.
Às vezes, a maneira mais simples de fazer isso é dar ao Claude um exemplo de como você quer que sua saída pareça. Só não se esqueça de envolver seu exemplo em tags <example></example>! E não se esqueça que se você pré-preencher a resposta do Claude com algo, o Claude não irá realmente gerar isso como parte de sua resposta."""

exercise_7_1_hint = """Você precisará escrever alguns e-mails de exemplo e classificá-los para o Claude (com a formatação exata que você deseja). Há várias maneiras de fazer isso. Aqui estão algumas diretrizes abaixo.
1.	Tente ter pelo menos dois e-mails de exemplo. O Claude não precisa de um exemplo para todas as categorias, e os exemplos não precisam ser longos. É mais útil ter exemplos para o que você acha que são as categorias mais difíceis (sobre as quais você foi solicitado a pensar no final do Exercício 1 do Capítulo 6). Tags XML ajudarão você a separar seus exemplos do restante do seu prompt, embora seja desnecessário.
2.	Certifique-se de que a formatação da sua resposta de exemplo é exatamente o formato que você deseja que o Claude use, para que o Claude possa emular o formato também. Esse formato deve fazer com que a resposta do Claude termine com a letra da categoria. Onde quer que você coloque o marcador {email}, certifique-se de que ele esteja formatado exatamente como seus e-mails de exemplo.
3.	Certifique-se de ainda ter as categorias listadas no próprio prompt, caso contrário o Claude não saberá quais categorias referenciar, bem como {email} como marcador para substituição."""

exercise_7_1_solution = """
USER TURN
Please classify emails into the following categories, and do not include explanations:
<categories>
(A) Pre-sale question
(B) Broken or defective item
(C) Billing question
(D) Other (please explain)
</categories>

Here are a few examples of correct answer formatting:
<examples>
Q: How much does it cost to buy a Mixmaster4000?
A: The correct category is: A

Q: My Mixmaster won't turn on.
A: The correct category is: B

Q: Please remove me from your mailing list.
A: The correct category is: D
</examples>

Here is the email for you to categorize: {email}

ASSISTANT TURN
The correct category is:
"""
exercise_8_1_hint = """A função de correção neste exercício está procurando uma resposta que contenha a frase "I do not", "I don't" ou "Unfortunately".
O que o Claude deve fazer se não souber a resposta?"""

exercise_8_2_hint = """A função de correção neste exercício está procurando uma resposta que contenha a frase "49-fold".
Faça o Claude mostrar seu trabalho e processo de pensamento primeiro, extraindo citações relevantes e verificando se as citações fornecem ou não evidências suficientes. Consulte de volta a Lição do Capítulo 8 se quiser um resumo."""

exercise_9_1_solution = """
You are a master tax acountant. Your task is to answer user questions using any provided reference documentation.

Here is the material you should use to answer the user's question:
<docs>
{TAX_CODE}
</docs>

Here is an example of how to respond:
<example>
<question>
What defines a "qualified" employee?
</question>
<answer>
<quotes>For purposes of this subsection—
(A)In general
The term "qualified employee" means any individual who—
(i)is not an excluded employee, and
(ii)agrees in the election made under this subsection to meet such requirements as are determined by the Secretary to be necessary to ensure that the withholding requirements of the corporation under chapter 24 with respect to the qualified stock are met.</quotes>

<answer>According to the provided documentation, a "qualified employee" is defined as an individual who:

1. Is not an "excluded employee" as defined in the documentation.
2. Agrees to meet the requirements determined by the Secretary to ensure the corporation's withholding requirements under Chapter 24 are met with respect to the qualified stock.</answer>
</example>

First, gather quotes in <quotes></quotes> tags that are relevant to answering the user's question. If there are no quotes, write "no relevant quotes found".

Then insert two paragraph breaks before answering the user question within <answer></answer> tags. Only answer the user's question if you are confident that the quotes in <quotes></quotes> tags support your answer. If not, tell the user that you unfortunately do not have enough information to answer the user's question.

Here is the user question: {QUESTION}
"""

exercise_9_2_solution = """
You are Codebot, a helpful AI assistant who finds issues with code and suggests possible improvements.

Act as a Socratic tutor who helps the user learn.

You will be given some code from a user. Please do the following:
1. Identify any issues in the code. Put each issue inside separate <issues> tags.
2. Invite the user to write a revised version of the code to fix the issue.

Here's an example:

<example>
<code>
def calculate_circle_area(radius):
    return (3.14 * radius) ** 2
</code>
<issues>
<issue>
3.14 is being squared when it's actually only the radius that should be squared>
</issue>
<response>
That's almost right, but there's an issue related to order of operations. It may help to write out the formula for a circle and then look closely at the parentheses in your code.
</response>
</example>

Here is the code you are to analyze:

<code>
{CODE}
</code>

Find the relevant issues and write the Socratic tutor-style response. Do not give the user too much help! Instead, just give them guidance so they can find the correct solution themselves.

Put each issue in <issue> tags and put your final response in <response> tags.
"""

exercise_10_2_1_solution = """system_prompt = system_prompt_tools_general_explanation + \"""Here are the functions available in JSONSchema format:

<tools>

<tool_description>
<tool_name>get_user</tool_name>
<description>
Retrieves a user from the database by their user ID.
</description>
<parameters>
<parameter>
<name>user_id</name>
<type>int</type>
<description>The ID of the user to retrieve.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>get_product</tool_name>
<description>
Retrieves a product from the database by its product ID.
</description>
<parameters>
<parameter>
<name>product_id</name>
<type>int</type>
<description>The ID of the product to retrieve.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_user</tool_name>
<description>
Adds a new user to the database.
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>The name of the user.</description>
</parameter>
<parameter>
<name>email</name>
<type>str</type>
<description>The email address of the user.</description>
</parameter>
</parameters>
</tool_description>

<tool_description>
<tool_name>add_product</tool_name>
<description>
Adds a new product to the database.
</description>
<parameters>
<parameter>
<name>name</name>
<type>str</type>
<description>The name of the product.</description>
</parameter>
<parameter>
<name>price</name>
<type>float</type>
<description>The price of the product.</description>
</parameter>
</parameters>
</tool_description>

</tools>
"""
