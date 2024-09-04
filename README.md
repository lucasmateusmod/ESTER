**ESTER - Especialista em Síntese para Transcrição de Ementas e Resumos**
Desenvolvido por Lucas Mateus de Oliveira Duarte

Este repositório apresenta uma prototipação inicial destinada a demonstrar o potencial da ideia proposta.

O objetivo é automatizar a geração de ementas conforme o novo padrão do CNJ.

Os avanços contínuos nas aplicações e integrações de ferramentas baseadas em inteligência artificial generativa têm sido significativos. Nesse contexto, a ferramenta buscará utilizar a API de LLMs disponíveis no mercado, inicialmente a OpenAI, para gerar ementas a partir das decisões enviadas. O foco é otimizar os resultados da ferramenta por meio de ajuste fino, engenharia de prompts e técnicas de RAG.

Na API da OpenAI, os assistentes com a função de pesquisa de arquivos, utilizando uma base de dados vetorizada composta por exemplos de ementas e o manual de padronização de ementas do CNJ, alcançaram ementas no padrão ideal utilizando o modelo GPT-4 Mini. Outro ponto positivo deste recurso é a possibilidade de retroalimentação da base de dados vetorizada, uma vez que possibilita a adição de diversos arquivos. As ementas validadas poderão ser inseridas no banco de dados, otimizando a precisão da ferramenta. 

No padrão anterior, realizamos ajuste fino; no entanto, para o novo padrão, descartei a princípio o ajuste fino devido aos custos e às novas funcionalidades da OpenAI em análise, que resultaram em desempenho superior. Sugere-se a utilização desses novos recursos.

Junto com o prompt, encaminho também a aplicação Flask de demonstração.
