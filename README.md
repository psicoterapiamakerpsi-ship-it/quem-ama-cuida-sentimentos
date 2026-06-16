Monitoramento de audiência - Um estudo de recepção de telenovela no X
Disciplina: Dados, plataformas e métodos digitais.
Autora: Caroline Fortes Cabral; Emílio Negreiros; Lucas  Rosa
Ano: 2026
DOI: https://doi.org/10.5281/zenodo.20724008


Descrição

Este repositório reúne os dados processados, scripts e documentação metodológica de um estudo de recepção televisiva baseado em social listening. A pesquisa analisou o comportamento da audiência da telenovela Quem Ama Cuida (Rede Globo) no X (anteriormente Twitter) durante a exibição do primeiro capítulo, em 18 de maio de 2026, entre 21h20 e 22h10 (horário de Brasília).
O estudo investiga como a audiência reage em tempo real a uma narrativa televisiva, mapeando o sentimento expresso nas publicações — positivo, negativo e neutro — e cruzando essas reações com a divisão de cenas do capítulo. O objetivo central é demonstrar o potencial do social listening como ferramenta metodológica para pesquisa em comunicação e estudos de recepção.

Dados
ItemDescriçãoPlataformaX (Twitter)Hashtag monitorada#QuemAmaCuidaPeríodo de coleta18/05/2026, 21h20–22h10 (horário de Brasília)Total de publicações7.207 tweetsIdioma predominantePortuguês brasileiro
⚠️ Nota: os dados brutos (arquivo .ndjson) não estão incluídos neste repositório por restrições dos Termos de Serviço do X. Os dados processados e anonimizados estão disponíveis em resultado_sentimentos.csv.

Estrutura do Repositório

📁 quem-ama-cuida-sentimentos/
│
├── 📄 README.md                        — este arquivo
├── 📄 resultado_sentimentos.csv        — dados processados com classificação de sentimento
├── 📄 stopwords_removidas.xlsx         — documentação das stopwords removidas e nota metodológica
├── 🐍 teste.py                         — script principal de limpeza e análise de sentimento
├── 🐍 ajustar_data.py                  — script de conversão e ajuste de fuso horário
└── 📁 graficos/
    └── 🖼️ Minuto a minuto_sentimentos.png  — distribuição de sentimentos por minuto ao longo do capítulo

Gráficos
Sentimentos minuto a minuto

Mostrar Imagem
Evolução dos sentimentos positivo, negativo e neutro ao longo dos 50 minutos de exibição do primeiro capítulo, cruzada com a minutagem das cenas. O gráfico evidencia os picos de engajamento e a sincronização crescente entre a tensão narrativa e o comportamento da audiência nas redes sociais.


Metodologia Resumida
Coleta: dados coletados via 4CAT (Peeters & Hagen, 2022) com extensão Zeeschuimer.
Pré-processamento: limpeza dos textos em Python 3.14, com remoção de URLs, menções a usuários e hashtags. Scripts desenvolvidos com auxílio do modelo de linguagem Claude Sonnet (Anthropic, 2025).
Análise de sentimentos: classificação realizada via biblioteca pysentimiento (Pérez et al., 2021), desenvolvida para textos em português e espanhol.
Cruzamento: os resultados foram cruzados com a divisão manual de cenas do capítulo por núcleo narrativo e minutagem.
Para a documentação completa das stopwords removidas e decisões metodológicas, consulte stopwords_removidas.xlsx.


Como Reproduzir a Análise

Requisitos
Python 3.10 ou superior
Bibliotecas: pysentimiento, pandas

Instalação
bashpip install pysentimiento pandas
Execução
Adicione seu arquivo de dados como data.ndjson na raiz do repositório
Execute o script principal:
bashpython teste.py
O resultado será salvo em resultado_sentimentos.csv

Referências

ANTHROPIC. Claude (modelo de linguagem de grande escala). San Francisco, 2025. Disponível em: https://www.anthropic.com. Acesso em: jun. 2026.

PÉREZ, J. M. et al. pysentimiento: A Python toolkit for opinion mining and social NLP tasks. 2021. Disponível em: https://arxiv.org/abs/2106.09462. Acesso em: jun. 2026.

PEETERS, S.; HAGEN, S. The 4CAT Capture and Analysis Toolkit: A modular tool for transparent and traceable social media research. Journal of Open Humanities Data, v. 8, n. 24, 2022. Disponível em: https://doi.org/10.5334/johd.119. Acesso em: jun. 2026.

Licença
Este repositório está disponível sob a licença Creative Commons Zero v1.0 Universal (CC0-1.0). Você pode usar, adaptar e redistribuir o conteúdo livremente, inclusive para fins comerciais, sem necessidade de atribuição.
