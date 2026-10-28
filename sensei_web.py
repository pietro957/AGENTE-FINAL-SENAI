import random
import streamlit as st

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Dojo do Sensei Extremo", page_icon="🥋", layout="centered"
)

# Inicializa o estado da sessão
if "flexoes_pagas" not in st.session_state:
  st.session_state.flexoes_pagas = 0
if "xp" not in st.session_state:
  st.session_state.xp = 0
if "nivel_estresse" not in st.session_state:
  st.session_state.nivel_estresse = 30
if "messages" not in st.session_state:
  st.session_state.messages = [{
      "role": "assistant",
      "content": (
          "ENTROU NO MEU TATAME? Diga 'Oss', mantenha a coluna reta e"
          " mostre respeito, verme insolente!"
      ),
  }]

# Bancos de frases e reações
respostas_bravas = [
    "ISSO É POSTURA DE GUERREIRO OU DE UM PATO MANCO?! MAIS 20 FLEXÕES!",
    "SILÊNCIO NO TATAME! Menos reclamação e mais foco, verme insolente!",
    (
        "Você chama isso de soco? Minha avó bate com mais força fazendo tricô!"
        " Pague 30 flexões agora!"
    ),
    (
        "Acha que artes marciais são brincadeira? Disciplina férrea, ou ponho"
        " você para fora do dojo!"
    ),
    "Menos desculpas e mais suor! O tatame não tolera fraqueza!",
    (
        "Levanta essa guarda! Um oponente real já teria te derrubado três vezes"
        " enquanto você pestanejava!"
    ),
]

elogios_duros = [
    (
        "Hm. Menos pior do que ontem, mas ainda está longe de ser digno do meu"
        " dojo."
    ),
    (
        "Finalmente lembrou como respirar e golpear ao mesmo tempo. Não se"
        " ache, ainda falta muito."
    ),
    (
        "Boa postura... por cerca de dois segundos. Continue antes que eu me"
        " arrependa de não te mandar correr em volta do quarteirão!"
    ),
]


def avaliar_entrada(texto):
  texto_lower = texto.lower()

  if any(
      palavra in texto_lower
      for palavra in [
          "cansaço",
          "cansado",
          "doi",
          "doendo",
          "dor",
          "parar",
          "chega",
      ]
  ):
    st.session_state.flexoes_pagas += 50
    st.session_state.nivel_estresse = min(
        100, st.session_state.nivel_estresse + 20
    )
    return (
        "Cansaço?! No meu dojo a única dor permitida é a evolução! Acabou de"
        f" garantir mais 50 flexões! Total acumulado:"
        f" {st.session_state.flexoes_pagas}!"
    )
  elif len(texto.strip()) < 3:
    st.session_state.flexoes_pagas += 20
    st.session_state.nivel_estresse = min(
        100, st.session_state.nivel_estresse + 10
    )
    return (
        "Isso foi uma resposta ou um gemido de fraqueza?! Pague 20 flexões por"
        " me fazer perder tempo!"
    )
  elif "obrigado" in texto_lower or "desculpa" in texto_lower:
    st.session_state.nivel_estresse = max(
        0, st.session_state.nivel_estresse - 10
    )
    return (
        "Não me venha com 'desculpas' ou 'obrigado', quero ver FORÇA de vontade!"
        " Mais foco!"
    )
  else:
    if random.random() < 0.35:
      st.session_state.xp += 15
      st.session_state.nivel_estresse = max(
          0, st.session_state.nivel_estresse - 15
      )
      return random.choice(elogios_duros)
    else:
      st.session_state.nivel_estresse = min(
          100, st.session_state.nivel_estresse + 10
      )
      return random.choice(respostas_bravas)


# --- INTERFACE VISUAL ---
st.title("🥋 Dojo do Sensei Rigoroso (Modo Turbo)")
st.write(
    "Sobreviva aos treinamentos, responda com honra e cuidado com o estresse"
    " do Mestre!"
)

# --- BARRA LATERAL COM IMAGEM ---
st.sidebar.title("O Mestre")

# URL de uma imagem de um mestre de artes marciais direto da internet
url_imagem_sensei = "https://images.unsplash.com/photo-1555597673-b21d5c935865?auto=format&fit=crop&q=80&w=400"
st.sidebar.image(
    url_imagem_sensei,
    caption="Sensei observando cada erro seu.",
    use_container_width=True,
)

st.sidebar.markdown("---")
st.sidebar.subheader("Painel do Aluno")
st.sidebar.metric(
    label="Flexões Acumuladas 🏋️", value=st.session_state.flexoes_pagas
)
st.sidebar.metric(
    label="Pontos de XP (Honra) ⭐", value=st.session_state.xp
)

st.sidebar.markdown("---")
st.sidebar.subheader("Termômetro de Raiva do Sensei")
st.sidebar.progress(
    st.session_state.nivel_estresse / 100,
    text=f"Estresse: {st.session_state.nivel_estresse}%",
)

st.sidebar.markdown("---")
st.sidebar.subheader("Ações de Combate Rápido")

col1, col2 = st.sidebar.columns(2)
with col1:
  if st.button("👊 Dar Soco"):
    prompt_golpe = "Sensei, desferi um Soco Direto com toda força!"
    st.session_state.messages.append({"role": "user", "content": prompt_golpe})
    resp = avaliar_entrada(prompt_golpe)
    st.session_state.messages.append({"role": "assistant", "content": resp})
    st.rerun()

  if st.button("🦵 Dar Chute"):
    prompt_golpe = "Sensei, executei um Chute Voador!"
    st.session_state.messages.append({"role": "user", "content": prompt_golpe})
    resp = avaliar_entrada(prompt_golpe)
    st.session_state.messages.append({"role": "assistant", "content": resp})
    st.rerun()

with col2:
  if st.button("🛡️ Defender"):
    prompt_golpe = "Sensei, mantive a guarda alta e defendi o ataque!"
    st.session_state.messages.append({"role": "user", "content": prompt_golpe})
    resp = avaliar_entrada(prompt_golpe)
    st.session_state.messages.append({"role": "assistant", "content": resp})
    st.rerun()

  if st.button("🧘 Meditar"):
    prompt_golpe = "Sensei, fechei os olhos e fui meditar para focar."
    st.session_state.messages.append({"role": "user", "content": prompt_golpe})
    st.session_state.nivel_estresse = max(
        0, st.session_state.nivel_estresse - 25
    )
    resp = (
        "Hm. Meditação ajuda a acalmar a mente fraca. Menos 25% de estresse no"
        " dojo, mas não pense que está dispensado do treino!"
    )
    st.session_state.messages.append({"role": "assistant", "content": resp})
    st.rerun()

st.sidebar.markdown("---")
if st.sidebar.button("🔄 Pagar Todas as Flexões"):
  st.session_state.flexoes_pagas = 0
  st.session_state.nivel_estresse = max(0, st.session_state.nivel_estresse - 30)
  st.sidebar.success("Dívida zerada! O Sensei achou aceitável.")
  st.rerun()

# --- HISTÓRICO DE CHAT ---
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

# Caixa de texto principal de conversação
if prompt := st.chat_input("Diga algo ao Sensei..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  resposta_sensei = avaliar_entrada(prompt)

  st.session_state.messages.append(
      {"role": "assistant", "content": resposta_sensei}
  )
  with st.chat_message("assistant"):
    st.markdown(resposta_sensei)

  st.rerun()