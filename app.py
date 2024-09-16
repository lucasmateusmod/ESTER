from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

# Substitua pela sua chave da API OpenAI
api_key = "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"

# Endpoint da API da OpenAI
url = 'https://api.openai.com/v1/chat/completions'

def gerar_ementa(sentenca):
    prompt = f"""
    Contexto: O objetivo é gerar ementas padronizadas para decisões judiciais com base nas diretrizes estabelecidas no Manual de Padronização de Ementas. A ementa deve seguir a estrutura e as diretrizes descritas abaixo, garantindo clareza, concisão e uniformidade.

    Estrutura da Ementa:
    Cabeçalho (ou Indexação)
    Conteúdo: Área do direito; Tipo de ação; Tema geral; Complemento necessário; Solução do caso.
    Formatação: Preferencialmente em efeito versalete (small caps) ou CAPS LOCK. Máximo de quatro linhas.
    Exemplo: Ementa: Direito administrativo e previdenciário. Embargos de declaração em agravo interno em recurso extraordinário. Recurso protelatório. Embargos rejeitados.

    I. Caso em exame
    Conteúdo: Descrição sumária do caso, incluindo fatos relevantes e pedido principal.
    Formatação: Título em versalete e negrito. Texto ordenado por numerais cardinais. Pode ser dividido em parágrafos com subtítulos em itálico, se necessário.
    Exemplo: I. Caso em exame
    Embargos de declaração opostos em face de acórdão que negou provimento a agravo interno, mantendo a decisão de inadmissão do recurso extraordinário, com fundamento nas Súmulas nº 279 e nº 280/STF.

    II. Questão em discussão
    Conteúdo: Breve relato das questões controvertidas e suas fundamentações.
    Formatação: Título em versalete e negrito. Texto ordenado por numerais cardinais e numeração romana para questões múltiplas.
    Exemplo: II. Questão em discussão
    A questão em discussão consiste em saber se há obscuridade, contradição ou omissão que justifique (i) o afastamento de multa prevista no § 4º do art. 1.021 do CPC e (ii) a redução de honorários fixados por ocasião do julgamento do agravo interno.

    III. Razões de decidir
    Conteúdo: Resumo dos principais fundamentos da decisão, um fundamento por item.
    Formatação: Título em versalete e negrito. Texto ordenado por numerais cardinais.
    Exemplo: III. Razões de decidir
    Os embargos não apontam qualquer erro, obscuridade, contradição ou omissão no acórdão embargado, o que afasta a presença dos pressupostos de embargabilidade do art. 1.022 do CPC.

    IV. Dispositivo e tese
    Conteúdo: Conclusão da decisão e, se aplicável, tese de julgamento.
    Formatação: Título em versalete e negrito. Tese, se houver, precedida de subtítulo em itálico. Ordenação por numerais cardinais.
    Exemplo: IV. Dispositivo e tese
    Embargos de declaração rejeitados.

    Legislação e jurisprudência relevantes citadas
    Conteúdo: Citação de dispositivos legais e jurisprudência relevante para a decisão.
    Formatação: Títulos em itálico. Utilizar ponto e vírgula para separação de diplomas normativos e vírgula para dispositivos. Usar abreviaturas padronizadas.
    Exemplo:
    Dispositivos relevantes citados: CPC, arts. 1.021, § 4º, e 1.022.
    Jurisprudência relevante citada: STF, AgR no ARE 822.641, Rel. Min. Edson Fachin, 1ª Turma, j. 23.10.2015.

    Orientações Gerais:
    Frases curtas e claras, sem uso exagerado de vírgulas e apóstrofos.
    Ordem direta das orações.
    Sem citações doutrinárias, adjetivos, advérbios ou sinônimos.
    Seguir as abreviações e denominações padronizadas.
    Objetivo: Gerar uma ementa que siga rigorosamente o padrão descrito, com clareza e precisão, e que facilite a busca e análise por meio de inteligência artificial.

    Gerar uma ementa com base na sentença a seguir:
    {sentenca}
    """

    data = {
        
        
        
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1500,
        "temperature": 0.5
    }

    headers = {
        'Authorization': f'Bearer {api_key}',
        "OpenAI-Beta": "assistants=v2",
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = response.json()
        ementa = response_json['choices'][0]['message']['content']
        return ementa
    else:
        return f"Erro na solicitação: {response.status_code} - {response.text}"

@app.route("/", methods=["GET", "POST"])
def index():
    ementa = ""
    if request.method == "POST":
        sentenca = request.form["sentenca"]
        ementa = gerar_ementa(sentenca)
    return render_template("index.html", ementa=ementa)

if __name__ == "__main__":
    app.run(debug=True)
