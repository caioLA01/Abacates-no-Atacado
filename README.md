# Abacates-no-Atacado

O Programa se refere a um site de analise de imagens de máquinas industriais para relacioná-las a uma tabela de expecificações.

# Interface

Para realizar as análises é necessário fazer o download de pelo menos um arquivo de imagem, mas ele consegue receber até 3 imagens, com 1 referente à placa de identificação da máquina e outras duas da máquina em si e um arquivo .json também referente à identificação da máquina.

Após o upload dos arquivos o programa irá mostrar as especificações referentes às imagens ou uma mensagem de erro caso as imagens não estejam coerentes

A base da interface foi feita usando html e css

# Programa

Os códigos por trás se baseiam no uso da API da openAI referente ao chat-gpt

O programa recebe os arquivos que foram carregados no site e manda-os para o chat-gpt analisar. Nessa análise será considerada se as imagens enviadas são suficientes para que as especificações sejam geradas, se não forem ele irá tentar novamente uma vez e caso continuem insatisfatórias ele irá informar ao usuário que os arquivos enviados não são referentes a uma das máquinas do banco de dados.

Se as imagens forem possíveis de serem analisadas o programa então irá pedir ao GPT para gerar as especificações da máquina em questão sendo elas: Nome, Modelo, Nº de identificação, Fabricante, Potência, Rotação, Tensão, Grau de Proteção e Eficiência. 