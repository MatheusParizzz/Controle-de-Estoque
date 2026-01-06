import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date

# JANELA
janela = tk.Tk()
janela.title("Controle de Uniformes e EPIs")
janela.state("zoomed")
janela.geometry("1080x600")
janela.minsize(1080, 600)
janela.resizable(True, True)
janela.configure(background="#f0f0f0")
janela.iconbitmap(r"assets\icone_app.ico")

# CONFIGURAÇÕES / PREDEFINIÇÕES DE ESTILO
style = ttk.Style()
style.theme_use("vista")

style.configure("TNotebook.Tab",
                focuscolor="none",
                focusthickness=0,
                padding=[10, 12])

style.configure(
    "SubNotebook.TNotebook.Tab",
    padding=5)

style.configure("TEntry",
                padding=5)

style.configure("TCombobox",
                padding=5)

style.configure("TButton",
                padding=5)

cor_chave = "#5798C0"
nome_da_empresa = "Nome da Empresa"

# CRIA OS PAINÉIS (REDIMENSIONÁVEIS)
painel_janela = tk.PanedWindow(
    janela,
    orient=tk.HORIZONTAL,
    sashwidth=2
)
painel_janela.pack(fill="both", expand=True)

painel_barra_lateral = tk.PanedWindow(
    painel_janela,
    orient=tk.VERTICAL,
    sashwidth=2
)
painel_janela.add(painel_barra_lateral, minsize=230)

painel_notebook = tk.PanedWindow(
    painel_janela,
    orient=tk.VERTICAL,
    sashwidth=2
)
painel_janela.add(painel_notebook)

# CRIA O NOTEBOOK
notebook = ttk.Notebook(painel_notebook)
notebook.pack(expand=True, fill='both', side='right', padx=10)
painel_notebook.add(notebook)

# ==============================================================================
# 01. PÁGINA ESTOQUE DO NOTEBOOK
# ==============================================================================
img_estoque = tk.PhotoImage(file=r"assets\icone_estoque.png")
pagina_estoque = ttk.Frame(notebook)
pagina_estoque.grid_columnconfigure(0, weight=1)
pagina_estoque.grid_rowconfigure(2, weight=1)
notebook.add(pagina_estoque, text="Estoque", image=img_estoque, compound="left") # ADICIONO A PÁGINA ESTOQUE AO NOTEBOOK

# TÍTULO
titulo = ttk.Label(pagina_estoque, text="Controle de Estoque", font=("Aptos", 26, "bold"), foreground=cor_chave)
titulo.grid(row=0, column=0, sticky="w", pady=(10, 0), padx=(10, 0))
# SUBTÍTULO
subtitulo = ttk.Label(pagina_estoque, text=nome_da_empresa, font=("Aptos", 9), foreground=cor_chave)
subtitulo.grid(row=1, column=0, sticky="w", pady=(0, 10), padx=(10, 0))

# SUBNOTEBOOK DENTRO DA PÁGINA ESTOQUE
notebook_pagina_estoque = ttk.Notebook(pagina_estoque, style="SubNotebook.TNotebook") # CRIO UM NOVO NOTEBOOK DENTRO DA PÁGINA ESTOQUE
notebook_pagina_estoque.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=(0, 5), padx=5)

# 01.1 SUBPÁGINA RELATÓRIO =====================================================
subpagina_relatorio = ttk.Frame(notebook_pagina_estoque)
subpagina_relatorio.grid_columnconfigure(0, weight=1)
subpagina_relatorio.grid_rowconfigure(2, weight=1)
notebook_pagina_estoque.add(subpagina_relatorio, text="Relatório") # ADICIONO A SUBPÁGINA RELATÓRIO AO NOTEBOOK PÁGINA ESTOQUE

# CABEÇALHO
cabecalho = tk.Frame(subpagina_relatorio)
cabecalho.grid(row=0, column=0, sticky='ew')

# BOTÃO EXPORTAR
button_relatorio = ttk.Button(cabecalho, text="Exportar", width=25)
button_relatorio.grid(row=0, column=0, pady=(10, 0), padx=10, sticky="e")

# FILTROS
filtros = tk.LabelFrame(subpagina_relatorio, text="Filtros")
filtros.grid(row=1, column=0, columnspan=2, pady=(5, 10), padx=10, sticky="ew")
# -- PRODUTO
label_produto = ttk.Label(filtros, text="Produto:")
label_produto.pack(fill="x", side="left", padx=10, pady=(5, 10))
entry_busca = ttk.Entry(filtros)
entry_busca.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10), expand=True)
# -- CATEGORIA
label_categoria = ttk.Label(filtros, text="Categoria:")
label_categoria.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
combobox_categoria = ttk.Combobox(filtros, values=["UNIF. SUPERIOR", "UNIF. INFERIOR", "EPI - CALÇADO", "EPI - OUTRO"], state="readonly")
combobox_categoria.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10), expand=True)
# -- STATUS
label_status = ttk.Label(filtros, text="Status:")
label_status.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
combobox_status = ttk.Combobox(filtros, values=["ESTOQUE EXCESSIVO", "ESTOQUE ADEQUADO", "ESTOQUE MÍNIMO", "ESTOQUE ZERADO"], state="readonly")
combobox_status.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10), expand=True)
# -- BOTÃO BUSCAR
button_buscar = ttk.Button(filtros, text="Buscar", width=10)
button_buscar.pack(fill="x", side="right", padx=(0, 10), pady=(5, 10))

# TABELA ESTOQUE
tabela_estoque = ttk.Treeview(subpagina_relatorio, columns=("ID", "Produto", "Disponível", "Pendente", "Status"), show="headings", height=24)
tabela_estoque.heading("ID", text="ID")
tabela_estoque.column("ID", width=20, anchor="center", stretch=False)
tabela_estoque.heading("Produto", text="Produto")
tabela_estoque.column("Produto", width=400, anchor="center")
tabela_estoque.heading("Disponível", text="Disponível")
tabela_estoque.column("Disponível", width=100, anchor="center")
tabela_estoque.heading("Pendente", text="Pendente")
tabela_estoque.column("Pendente", width=100, anchor="center")
tabela_estoque.heading("Status", text="Status")
tabela_estoque.column("Status", width=120, anchor="center")
tabela_estoque.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nsew")

# 01.2 SUBPÁGINA TRANSAÇÕES ====================================================
subpagina_transacoes = ttk.Frame(notebook_pagina_estoque)
notebook_pagina_estoque.add(subpagina_transacoes, text="Transações") # ADICIONO A SUBPÁGINA TRANSAÇÕES AO NOTEBOOK PÁGINA ESTOQUE

# BOTÃO LANÇAR TRANSAÇÃO 
button_lancar_transacao = ttk.Button(subpagina_transacoes, text="Lançar", width=25, command=lambda:abrir_janela_lancar_transacao())
button_lancar_transacao.grid(row=0, column=0, pady=(10, 0), padx=10, sticky="e")
# BOTÃO EXPORTAR
button_relatorio = ttk.Button(subpagina_transacoes, text="Exportar", width=25)
button_relatorio.grid(row=0, column=1, pady=(10, 0), padx=(0, 10), sticky="e")

# ==============================================================================
# 02. PÁGINA SOLICITAÇÕES DO NOTEBOOK
# ==============================================================================
img_solicitacoes = tk.PhotoImage(file=r"assets\icone_solicitacoes.png")
pagina_solicitacoes = ttk.Frame(notebook)
pagina_solicitacoes.grid_columnconfigure(0, weight=1)
pagina_solicitacoes.grid_rowconfigure(4, weight=1)
notebook.add(pagina_solicitacoes, text="Solicitações", image=img_solicitacoes, compound="left")

# CABEÇALHO
cabecalho = tk.Frame(pagina_solicitacoes)
cabecalho.grid(row=0, column=0, sticky='ew')
cabecalho.columnconfigure(1, weight=1)

titulo = ttk.Label(cabecalho, text="Controle de Solicitações", font=("Aptos", 26, "bold"), foreground=cor_chave)
titulo.grid(row=0, column=0, sticky="w", pady=(10, 0), padx=(10, 0))

subtitulo = ttk.Label(cabecalho, text=nome_da_empresa, font=("Aptos", 9), foreground=cor_chave)
subtitulo.grid(row=1, column=0, sticky="w", pady=(0, 10), padx=(10, 0))

# FRAME DOS BOTÕES
frame_botoes = ttk.Frame(cabecalho)
frame_botoes.grid(row=2, column=0, sticky="ew")
# -- BOTÃO SEPARAR
button_separar = ttk.Button(frame_botoes, text="Separar", width=20)
button_separar.grid(row=0, column=0, pady=(0, 5), padx=(10, 10), sticky="e")
# -- BOTÃO DESPACHAR
button_despachar = ttk.Button(frame_botoes, text="Despachar", width=20)
button_despachar.grid(row=0, column=1, pady=(0, 5), padx=(0, 10), sticky="e")

# FILTROS
filtros_solicitacao = tk.LabelFrame(pagina_solicitacoes, text="Filtros")
filtros_solicitacao.grid(row=3, column=0, columnspan=2, pady=(0, 10), padx=10, sticky="ew")
linha1 = tk.Frame(filtros_solicitacao)
linha1.pack(fill="x", side="top")
linha2 = tk.Frame(filtros_solicitacao)
linha2.pack(fill="x", side="bottom")
# -- UNIDADE
label_unidade = ttk.Label(linha1, text="Unidade:")
label_unidade.pack(fill="x", side="left", padx=10, pady=(5, 10))
entry_unidade = ttk.Combobox(linha1, state="readonly", width=7, values=["CD", "LOJA 01", "LOJA 02", "LOJA 03", "LOJA 04", "LOJA 05", "LOJA 06", "LOJA 07", "LOJA 08", "LOJA 09", "LOJA 10"])
entry_unidade.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
# -- SOLICITAÇÃO
label_solicitacao = ttk.Label(linha1, text="Solicitação:")
label_solicitacao.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
entry_solicitacao = ttk.Entry(linha1, width=6)
entry_solicitacao.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
# -- EMPREGADO
label_empregado = ttk.Label(linha1, text="Empregado:")
label_empregado.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
entry_empregado = ttk.Entry(linha1)
entry_empregado.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10), expand=True)
# -- PRODUTO
label_produto = ttk.Label(linha1, text="Produto:")
label_produto.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
combobox_produto = ttk.Combobox(linha1)
combobox_produto.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10), expand=True)
# -- FINALIDADE
label_finalidade = ttk.Label(linha2, text="Finalidade:")
label_finalidade.pack(fill="x", side="left", padx=10, pady=(5, 10))
combobox_finalidade = ttk.Combobox(linha2, values=["ADM. LOJAS", "ADM. CD", "REP. LOJAS", "REP. CD"], state="readonly")
combobox_finalidade.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10), expand=True)
# -- STATUS
label_status = ttk.Label(linha2, text="Status:")
label_status.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
combobox_status = ttk.Combobox(linha2, values=["PENDENTE", "EM SEPARAÇÃO", "DESPACHADO"], state="readonly")
combobox_status.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10), expand=True)
combobox_status.set("PENDENTE")
# -- DATA
label_data_inicio = ttk.Label(linha2, text="De:")
label_data_inicio.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
data_inicio = DateEntry(linha2, width=8, date_pattern="dd/mm/yy", locale="pt_BR")
data_inicio.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
data_inicio.set_date(date(2026, 1, 1))
label_data_final = ttk.Label(linha2, text="Até:")
label_data_final.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
data_final = DateEntry(linha2, width=8, date_pattern="dd/mm/yy", locale="pt_BR")
data_final.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
# -- BOTÃO BUSCAR
button_buscar = ttk.Button(linha2, text="Buscar", width=20)
button_buscar.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))

# TABELA SOLICITAÇÕES + TABELA PRODUTOS
tabela_solicitacoes = ttk.Treeview(pagina_solicitacoes, columns=("ID", "Unidade", "Solic.", "Empregado", "Cargo", "Finalidade", "Data"), show="headings", height=10)
tabela_solicitacoes.heading("ID", text="ID")
tabela_solicitacoes.column("ID", width=60, anchor="center", stretch=False)
tabela_solicitacoes.heading("Unidade", text="Unidade")
tabela_solicitacoes.column("Unidade", width=60, anchor="center", stretch=False)
tabela_solicitacoes.heading("Solic.", text="Solic.")
tabela_solicitacoes.column("Solic.", width=60, anchor="center", stretch=False)
tabela_solicitacoes.heading("Empregado", text="Empregado")
tabela_solicitacoes.column("Empregado", width=50, anchor="center")
tabela_solicitacoes.heading("Cargo", text="Cargo")
tabela_solicitacoes.column("Cargo", width=100, anchor="center")
tabela_solicitacoes.heading("Finalidade", text="Finalidade")
tabela_solicitacoes.column("Finalidade", width=20, anchor="center")
tabela_solicitacoes.heading("Data", text="Data")
tabela_solicitacoes.column("Data", width=70, anchor="center", stretch=False)
tabela_solicitacoes.grid(row=4, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nsew")

tabela_produtos_solicitacoes = ttk.Treeview(pagina_solicitacoes, columns=("Categoria", "Produtos", "Qtd.", "Status"), show="headings", height=5)
tabela_produtos_solicitacoes.heading("Categoria", text="Categoria")
tabela_produtos_solicitacoes.column("Categoria", width=100, anchor="center", stretch=False)
tabela_produtos_solicitacoes.heading("Produtos", text="Produtos")
tabela_produtos_solicitacoes.column("Produtos", anchor="center")
tabela_produtos_solicitacoes.heading("Qtd.", text="Qtd.")
tabela_produtos_solicitacoes.column("Qtd.", width=30, anchor="center", stretch=False)
tabela_produtos_solicitacoes.heading("Status", text="Status")
tabela_produtos_solicitacoes.column("Status", width=150, anchor="center", stretch=False)
tabela_produtos_solicitacoes.grid(row=5, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nsew")

# ==============================================================================
# 03. PÁGINA DASHBOARDS DO NOTEBOOK
# ==============================================================================
img_dashboard = tk.PhotoImage(file=r"assets\icone_dashboard.png")
pagina_dashboards = ttk.Frame(notebook)
notebook.add(pagina_dashboards, text="Dashboards", image=img_dashboard, compound="left")

# CABEÇALHO
cabecalho = tk.Frame(pagina_dashboards)
cabecalho.grid(row=0, column=0, sticky='ew')
titulo = ttk.Label(cabecalho, text="Dashboards", font=("Aptos", 26, "bold"), foreground=cor_chave)
titulo.grid(row=0, column=1, sticky="w", pady=(10, 0), padx=(10, 0))
subtitulo = ttk.Label(cabecalho, text=nome_da_empresa, font=("Aptos", 9), foreground=cor_chave)
subtitulo.grid(row=1, column=1, sticky="w", pady=(0, 10), padx=(10, 0))

# ==============================================================================
# 04. PÁGINA PRODUTOS
# ==============================================================================
img_produtos = tk.PhotoImage(file=r"assets\icone_produtos.png")
pagina_produtos = ttk.Frame(notebook)
notebook.add(pagina_produtos, text="Produtos", image=img_produtos, compound="left")

# CABEÇALHO
cabecalho = tk.Frame(pagina_produtos)
cabecalho.grid(row=0, column=0, sticky='ew')
titulo = ttk.Label(cabecalho, text="Produtos", font=("Aptos", 26, "bold"), foreground=cor_chave)
titulo.grid(row=0, column=1, sticky="w", pady=(10, 0), padx=(10, 0))
subtitulo = ttk.Label(cabecalho, text=nome_da_empresa, font=("Aptos", 9), foreground=cor_chave)
subtitulo.grid(row=1, column=1, sticky="w", pady=(0, 10), padx=(10, 0))

# ==============================================================================
# 05. PÁGINA FORNECEDORES
# ==============================================================================
img_fornecedores = tk.PhotoImage(file=r"assets\icone_fornecedores.png")
pagina_fornecedores = ttk.Frame(notebook)
notebook.add(pagina_fornecedores, text="Fornecedores", image=img_fornecedores, compound="left")

# CABEÇALHO
cabecalho = tk.Frame(pagina_fornecedores)
cabecalho.grid(row=0, column=0, sticky='ew')
titulo = ttk.Label(cabecalho, text="Fornecedores", font=("Aptos", 26, "bold"), foreground=cor_chave)
titulo.grid(row=0, column=1, sticky="w", pady=(10, 0), padx=(10, 0))
subtitulo = ttk.Label(cabecalho, text=nome_da_empresa, font=("Aptos", 9), foreground=cor_chave)
subtitulo.grid(row=1, column=1, sticky="w", pady=(0, 10), padx=(10, 0))

# ==============================================================================
# 06. PÁGINA UNIDADES
# ==============================================================================
img_unidades = tk.PhotoImage(file=r"assets\icone_unidades.png")
pagina_unidades = ttk.Frame(notebook)
notebook.add(pagina_unidades, text="Unidades", image=img_unidades, compound="left")

# CABEÇALHO
cabecalho = tk.Frame(pagina_unidades)
cabecalho.grid(row=0, column=0, sticky='ew')
titulo = ttk.Label(cabecalho, text="Unidades", font=("Aptos", 26, "bold"), foreground=cor_chave)
titulo.grid(row=0, column=1, sticky="w", pady=(10, 0), padx=(10, 0))
subtitulo = ttk.Label(cabecalho, text=nome_da_empresa, font=("Aptos", 9), foreground=cor_chave)
subtitulo.grid(row=1, column=1, sticky="w", pady=(0, 10), padx=(10, 0))

# ==============================================================================
# 07. BARRA LATERAL
# ==============================================================================
barra_lateral = tk.Frame(painel_barra_lateral, width=260, background=cor_chave)
barra_lateral.pack_propagate(False)
# 07.1 LOGO
imagem = tk.PhotoImage(file=r"assets\logo.png")
logo = tk.Label(barra_lateral, image=imagem, bd=0, background=cor_chave)
logo.pack(pady=(20, 0))
# 07.2 TEXTO DO LOGO
logo_titulo = ttk.Label(barra_lateral, text="- CONTROLE -\nUNIFORMES E EPIS", font=("Aptos", 16, "bold"), foreground="#FFFFFF", background=cor_chave, justify="center")
logo_titulo.pack(pady=(20, 0))

logo_subtitulo = ttk.Label(barra_lateral, text=nome_da_empresa, font=("Aptos", 9), foreground="#FFFFFF", background=cor_chave, justify="center")
logo_subtitulo.pack()
# 07.3 SEPARADOR
separador = ttk.Separator(barra_lateral, orient='horizontal')
separador.pack(fill="both", pady=(20, 20), padx=18)
# 07.4 BOTÕES DE CADASTRO
button_produtos = ttk.Button(barra_lateral, text="Cadastrar Produto", width=25, command=lambda:abrir_janela_cadastrar_produto())
button_produtos.pack(pady=(0, 10))
button_cadastrar_fornecedor = ttk.Button(barra_lateral, text="Cadastrar Fornecedor", width=25, command=lambda:abrir_janela_cadastrar_fornecedor())
button_cadastrar_fornecedor.pack(pady=(0, 10))
button_cadastrar_unidade = ttk.Button(barra_lateral, text="Cadastrar Unidade", width=25, command=lambda:abrir_janela_cadastrar_unidade())
button_cadastrar_unidade.pack()
# 07.5 SEPARADOR
separador = ttk.Separator(barra_lateral, orient='horizontal')
separador.pack(fill="both", pady=(20, 20), padx=18)
# 07.6 BOTÕES DE LANÇAMENTOS
button_lancar_transacao = ttk.Button(barra_lateral, text="Lançar Transação", width=25, command=lambda:abrir_janela_lancar_transacao())
button_lancar_transacao.pack(pady=(0, 10))
button_lancar_solicitacao = ttk.Button(barra_lateral, text="Lançar Solicitação", width=25, command=lambda: abrir_janela_lancar_solicitacao())
button_lancar_solicitacao.pack()
# 07.7 SEPARADOR
separador = ttk.Separator(barra_lateral, orient='horizontal')
separador.pack(fill="both", pady=(20, 20), padx=18)
# 07.7 BOTÃO DE EXPORTAR RELATÓRIOS 
button_relatorio = ttk.Button(barra_lateral, text="Exportar", width=25)
button_relatorio.pack()
# 07.8 CRÉDITOS
credito = ttk.Label(barra_lateral, text="Feito por @MatheusParizz", background=cor_chave, foreground="white")
credito.pack(side="bottom", pady=(0, 10))

painel_barra_lateral.add(barra_lateral)
# ==============================================================================
# FUNÇÕES
# ==============================================================================
produtos = []
def abrir_janela_cadastrar_produto():
    button_produtos.config(state="disabled")
    janela_cadastrar_produto = tk.Toplevel(janela)
    janela_cadastrar_produto.title("Cadastrar Produto")
    janela_cadastrar_produto.resizable(False, False)
    janela_cadastrar_produto.iconbitmap(r"assets\icone_cadastrar.ico")
    janela_cadastrar_produto.transient(janela)
    centralizar(janela_cadastrar_produto)

    def fechar_janela():
        janela_cadastrar_produto.destroy()
        button_produtos.config(state="normal")
    janela_cadastrar_produto.protocol("WM_DELETE_WINDOW", fechar_janela)

    # DESCRIÇÃO
    labelframe_descricao = ttk.LabelFrame(janela_cadastrar_produto, text="Descricão*")
    labelframe_descricao.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 0))
    entry_descricao = ttk.Entry(labelframe_descricao)
    entry_descricao.pack(fill="x", padx=10, pady=10)

    # SEXO
    labelframe_sexo = ttk.LabelFrame(janela_cadastrar_produto, text="Sexo*")
    labelframe_sexo.grid(row=1, column=0, sticky="ew", padx=(10, 5))
    combobox_sexo = ttk.Combobox(labelframe_sexo, values=["MASC", "FEM", "UNISEX"], state="readonly")
    combobox_sexo.pack(fill="x", padx=10, pady=10)

    # TAMANHO
    labelframe_tamanho = ttk.LabelFrame(janela_cadastrar_produto, text="Tamanho*")
    labelframe_tamanho.grid(row=1, column=1, sticky="ew", padx=(5, 10))
    entry_tamanho = ttk.Entry(labelframe_tamanho)
    entry_tamanho.pack(fill="x", padx=10, pady=10)

    # CATEGORIA
    labelframe_categoria = ttk.LabelFrame(janela_cadastrar_produto, text="Categoria*")
    labelframe_categoria.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10)
    combobox_categoria = ttk.Combobox(labelframe_categoria, values=["UNIF. SUPERIOR", "UNIF. INFERIOR", "EPI - CALÇADO", "EPI - OUTRO"], state="readonly")
    combobox_categoria.pack(fill="x", padx=10, pady=10)

    # ESTOQUE
    labelframe_estoque = ttk.LabelFrame(janela_cadastrar_produto, text="Estoque*")
    labelframe_estoque.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10)
    # -- ESTOQUE MÍNIMO
    label_estoque_minimo = ttk.Label(labelframe_estoque, text="Mínimo:")
    label_estoque_minimo.pack(fill="x", padx=(10, 0), pady=10, side="left")
    entry_estoque_minimo = ttk.Entry(labelframe_estoque)
    entry_estoque_minimo.pack(fill="x", padx=10, pady=10, side="left")
    # -- ESTOQUE IDEAL
    label_estoque_ideal = ttk.Label(labelframe_estoque, text="Ideal:")
    label_estoque_ideal.pack(fill="x", padx=(10, 0), pady=10, side="left")
    entry_estoque_ideal = ttk.Entry(labelframe_estoque)
    entry_estoque_ideal.pack(fill="x", padx=10, pady=10, side="left")

    # CÓDIGOS
    labelframe_codigos = ttk.LabelFrame(janela_cadastrar_produto, text="Códigos")
    labelframe_codigos.grid(row=4, column=0, columnspan=2, sticky="ew", padx=10)
    button_add_codigos = ttk.Button(labelframe_codigos, text="+", width=2, command=lambda:add_codigos())
    button_add_codigos.pack(side="left", padx=10, pady=10)
    entry_codigos = ttk.Entry(labelframe_codigos, width=10)
    entry_codigos.pack(side="left", padx=(0, 10), pady=10)
    
    entries_codigos = [entry_codigos]
    def add_codigos():
        if len(entries_codigos) < 4:
            entry = ttk.Entry(labelframe_codigos, width=10)
            entry.pack(side="left", padx=(0, 10), pady=10)
            entries_codigos.append(entry)
    
    # CADASTRAR
    button_cadastrar = ttk.Button(janela_cadastrar_produto, text="Cadastrar Produto", command=lambda:cadastrar_produto())
    button_cadastrar.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
    def cadastrar_produto():
        # VALIDAÇÃO DOS DADOS
        if (not entry_descricao.get() or not combobox_sexo.get() or not entry_tamanho.get() or not combobox_categoria.get() or not entry_estoque_minimo.get() or not entry_estoque_ideal.get()):
            messagebox.showwarning("Campos obrigatórios", "Todos os campos devem ser preenchidos.", parent=janela_cadastrar_produto)
        elif any(p["produto"] == entry_descricao.get().upper() + " " + combobox_sexo.get() + " " + entry_tamanho.get().upper() for p in produtos):
            messagebox.showwarning("Produto já cadastrado", f"O produto {entry_descricao.get().upper()} {combobox_sexo.get()} {entry_tamanho.get().upper()} ja foi cadastrado.", parent=janela_cadastrar_produto)
        else:
            # FORMATA OS DADOS DO PRODUTO
            id = len(produtos) + 1
            produto = entry_descricao.get().upper() + " " + combobox_sexo.get() + " " + entry_tamanho.get().upper()
            descricao = entry_descricao.get().upper()
            sexo = combobox_sexo.get()
            tamanho = entry_tamanho.get().upper()
            categoria = combobox_categoria.get()
            estoque_minimo = int(entry_estoque_minimo.get())
            estoque_ideal = int(entry_estoque_ideal.get())
            estoque_disponivel = 0
            estoque_pendente = estoque_ideal - estoque_disponivel
            status = "ESTOQUE ZERADO"
            codigos = [entry.get() for entry in entries_codigos if entry.get()]

            # ORGANIZA OS DADOS COMO UM DICIONÁRIO
            dados_produto = {"produto": produto,
                            "id": id,
                            "descricao": descricao,
                            "sexo": sexo,
                            "tamanho": tamanho,
                            "categoria": categoria,
                            "estoque_minimo": estoque_minimo,
                            "estoque_ideal": estoque_ideal,
                            "estoque_disponivel": estoque_disponivel,
                            "estoque_pendente": estoque_pendente,
                            "status": status,
                            "codigos": codigos}
            
            # CADASTRA NA LISTA DE PRODUTOS
            produtos.append(dados_produto)

            # CADASTRA EM ESTOQUE
            tabela_estoque.insert("", "end", iid=id, values=(dados_produto["id"],
                                                            dados_produto["produto"],
                                                            dados_produto["estoque_disponivel"],
                                                            dados_produto["estoque_pendente"],
                                                            dados_produto["status"]))
            
            # CADASTRA EM PRODUTOS

fornecedores = []
def abrir_janela_cadastrar_fornecedor():
    button_cadastrar_fornecedor.config(state="disabled")
    janela_cadastrar_fornecedor = tk.Toplevel(janela)
    janela_cadastrar_fornecedor.title("Cadastrar Fornecedor")
    janela_cadastrar_fornecedor.resizable(False, False)
    janela_cadastrar_fornecedor.iconbitmap(r"assets\icone_cadastrar.ico")
    janela_cadastrar_fornecedor.transient(janela)
    centralizar(janela_cadastrar_fornecedor)

    def fechar_janela():
        janela_cadastrar_fornecedor.destroy()
        button_cadastrar_fornecedor.config(state="normal")
    janela_cadastrar_fornecedor.protocol("WM_DELETE_WINDOW", fechar_janela)

    # RAZÃO SOCIAL
    labelframe_razao_social = ttk.LabelFrame(janela_cadastrar_fornecedor, text="Razão Social*")
    labelframe_razao_social.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 0))
    entry_razao_social = ttk.Entry(labelframe_razao_social)
    entry_razao_social.pack(fill="x", padx=10, pady=10)

    # CNPJ
    labelframe_cnpj = ttk.LabelFrame(janela_cadastrar_fornecedor, text="CNPJ")
    labelframe_cnpj.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10)
    entry_cnpj = ttk.Entry(labelframe_cnpj)
    entry_cnpj.pack(fill="x", padx=10, pady=10)

    # E-MAIL
    labelframe_contato = ttk.LabelFrame(janela_cadastrar_fornecedor, text="Contato")
    labelframe_contato.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10)
    
    labelframe_email = ttk.LabelFrame(labelframe_contato, text="E-mail", labelanchor="n")
    labelframe_email.pack(fill="x", side="left", padx=10, pady=(2, 10))
    entry_email = ttk.Entry(labelframe_email)
    entry_email.pack(fill="x", padx=10, pady=10)

    labelframe_telefone = ttk.LabelFrame(labelframe_contato, text="Telefone", labelanchor="n")
    labelframe_telefone.pack(fill="x", side="left", padx=(2, 10), pady=(2, 10))
    entry_telefone = ttk.Entry(labelframe_telefone)
    entry_telefone.pack(fill="x", padx=10, pady=10)

    # CADASTRAR
    button_cadastrar_fornecedor2 = ttk.Button(janela_cadastrar_fornecedor, text="Cadastrar Fornecedor", command=lambda:cadastrar_fornecedor())
    button_cadastrar_fornecedor2.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
    def cadastrar_fornecedor():
        print("funcionando")

unidades = ["CD",
            "LOJA 01",
            "LOJA 02",
            "LOJA 03",
            "LOJA 04",
            "LOJA 05",
            "LOJA 07",
            "LOJA 08",
            "LOJA 10",
            "LOJA 12",
            "LOJA 13",
            "LOJA 14",
            "LOJA 15",
            "LOJA 16",
            "LOJA 17",
            "LOJA 18",
            "LOJA 19",
            "LOJA 20",
            "LOJA 21",
            "LOJA 22",
            "LOJA 24",
            "LOJA 25",
            "LOJA 26",
            "LOJA 27"]
def abrir_janela_cadastrar_unidade():
    button_cadastrar_unidade.config(state="disabled")
    janela_cadastrar_unidade = tk.Toplevel(janela)
    janela_cadastrar_unidade.title("Cadastrar Unidade")
    janela_cadastrar_unidade.resizable(False, False)
    janela_cadastrar_unidade.iconbitmap(r"assets\icone_cadastrar.ico")
    janela_cadastrar_unidade.transient(janela)
    centralizar(janela_cadastrar_unidade)

    def fechar_janela():
        janela_cadastrar_unidade.destroy()
        button_cadastrar_unidade.config(state="normal")
    janela_cadastrar_unidade.protocol("WM_DELETE_WINDOW", fechar_janela)

    # NOME
    labelframe_razao_social = ttk.LabelFrame(janela_cadastrar_unidade, text="Nome*")
    labelframe_razao_social.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 0))
    entry_razao_social = ttk.Entry(labelframe_razao_social)
    entry_razao_social.pack(fill="x", padx=10, pady=10)

    # CNPJ
    labelframe_cnpj = ttk.LabelFrame(janela_cadastrar_unidade, text="CNPJ")
    labelframe_cnpj.grid(row=1, column=0, sticky="ew", padx=10)
    entry_cnpj = ttk.Entry(labelframe_cnpj)
    entry_cnpj.pack(fill="x", padx=10, pady=10)

    # E-MAIL
    labelframe_email = ttk.LabelFrame(janela_cadastrar_unidade, text="E-mail")
    labelframe_email.grid(row=1, column=1, sticky="ew", padx=(2, 10))
    entry_email = ttk.Entry(labelframe_email)
    entry_email.pack(fill="x", padx=10, pady=10)

    # CADASTRAR
    button_cadastrar_fornecedor2 = ttk.Button(janela_cadastrar_unidade, text="Cadastrar Unidade", command=lambda:cadastrar_unidade())
    button_cadastrar_fornecedor2.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
    def cadastrar_unidade():
        print()

transacoes = []
def abrir_janela_lancar_transacao():
    button_lancar_transacao.config(state="disabled")
    janela_lancar_transacao = tk.Toplevel(janela)
    janela_lancar_transacao.title("Lançar Transação")
    janela_lancar_transacao.resizable(False, False)
    janela_lancar_transacao.iconbitmap(r"assets\icone_lancar.ico")
    janela_lancar_transacao.transient(janela)
    centralizar(janela_lancar_transacao)

    def fechar_janela():
        janela_lancar_transacao.destroy()
        button_lancar_transacao.config(state="normal")
    janela_lancar_transacao.protocol("WM_DELETE_WINDOW", fechar_janela)

    # CÓDIGO
    labelframe_codigo = ttk.LabelFrame(janela_lancar_transacao, text="Código*")
    labelframe_codigo.grid(row=0, column=0, padx=10, pady=(10, 0))
    entry_codigo = ttk.Entry(labelframe_codigo, width=10)
    entry_codigo.pack(side="left", padx=10, pady=10)

    # PRODUTO
    labelframe_produto = ttk.LabelFrame(janela_lancar_transacao, text="Produto")
    labelframe_produto.grid(row=0, column=1, padx=(2, 10), pady=(10, 0))
    entry_produto = ttk.Entry(labelframe_produto, state="disabled", width=50)
    entry_produto.pack(side="left", padx=10, pady=10)

    # ESTOQUE ATUAL
    labelframe_estoque_atual = ttk.LabelFrame(janela_lancar_transacao, text="Est. Atual")
    labelframe_estoque_atual.grid(row=0, column=2, padx=(2, 10), pady=(10, 0))
    entry_estoque_atual = ttk.Entry(labelframe_estoque_atual, state="disabled", width=10)
    entry_estoque_atual.pack(side="left", padx=10, pady=10)

    # QUANTIDADE
    labelframe_quantidade = ttk.LabelFrame(janela_lancar_transacao, text="Qtd.*")
    labelframe_quantidade.grid(row=1, column=0, padx=10, pady=(0, 10)) 
    entry_quantidade = ttk.Entry(labelframe_quantidade, width=10)
    entry_quantidade.pack(side="left", padx=10, pady=10)

    # C/V
    labelframe_compraouvenda = ttk.LabelFrame(janela_lancar_transacao, text="C/V*")
    labelframe_compraouvenda.grid(row=1, column=1, padx=(2, 10), pady=(0, 10), sticky="wens")

    opcao = tk.StringVar()

    entry_compra = ttk.Radiobutton(labelframe_compraouvenda, text="Compra", variable=opcao, value="compra")
    entry_compra.pack(side="left", padx=10, pady=10)

    entry_venda = ttk.Radiobutton(labelframe_compraouvenda, text="Venda", variable=opcao, value="venda")
    entry_venda.pack(side="left", padx=10, pady=10)

    # LANÇAR
    button_lancar_transacao2 = ttk.Button(janela_lancar_transacao, text="Confirmar", command=lambda:lancar_transacao())
    button_lancar_transacao2.grid(row=1, column=2, padx=(2, 10), pady=10, sticky="wens")
    def lancar_transacao():
        print()

solicitacoes = {
    "000001": {
        "solicitacao": "55001",
        "unidade": "CD",
        "empregado": "MATHEUS HENRIQUE",
        "cargo": "ASSIST. DE DEPTO. PESSOAL",
        "finalidade": "REP. CD",
        "data": "01/01/26",
        "produtos": [
            {"categoria": "UNIF. SUPERIOR",
             "produto":"CAMISA AZUL GG",
             "qtd": 3,
             "status": "PENDENTE"},
             
            {"categoria": "UNIF. INFERIOR",
             "produto":"CALÇA SOCIAL MASC 50",
             "qtd": 3,
             "status": "PENDENTE"},
        ]},
    "000002": {
        "solicitacao": "55001",
        "unidade": "CD",
        "empregado": "FULANO DE TAL",
        "cargo": "ASSIST. DE DEPTO. PESSOAL",
        "finalidade": "ADM. CD",
        "data": "01/01/26",
        "produtos": [
            {"categoria": "UNIF. SUPERIOR",
             "produto":"CAMISA BRANCA PP",
             "qtd": 3,
             "status": "PENDENTE"},

            {"categoria": "UNIF. INFERIOR",
             "produto":"CALÇA SOCIAL MASC 34",
             "qtd": 3,
             "status": "PENDENTE"},
        ]}}
def carregar_solicitacoes():
    for chave, dados in solicitacoes.items():
        tabela_solicitacoes.insert(
            "",
            "end",
            iid=chave,
            values=(
                chave,
                dados["unidade"],
                dados["solicitacao"],
                dados["empregado"],
                dados["cargo"],
                dados["finalidade"],
                dados["data"]
            ))
carregar_solicitacoes()
def carregar_produtos_solicitacao(event):
    selecionado = tabela_solicitacoes.focus()
    # LIMPA A TABELA PRODUTOS SOLICITAÇÕES
    for i in tabela_produtos_solicitacoes.get_children():
        tabela_produtos_solicitacoes.delete(i)
    # CARREGA OS PRODUTOS DA SOLICITAÇÃO SELECIONADA
    for produto in solicitacoes[selecionado]["produtos"]:
        categoria = list(produto.keys())[0]
        tabela_produtos_solicitacoes.insert(
            "",
            "end",
            values=(produto["categoria"], produto["produto"], produto["qtd"], produto["status"])
        )
tabela_solicitacoes.bind("<<TreeviewSelect>>", carregar_produtos_solicitacao) # CARREGA OS PRODUTOS QUANDO A SOLICITAÇÃO FOR SELECIONADA
def abrir_janela_lancar_solicitacao():
    button_lancar_solicitacao.config(state="disabled")
    janela_lancar_solicitacao = tk.Toplevel(janela)
    janela_lancar_solicitacao.title("Lançar Solicitação")
    janela_lancar_solicitacao.resizable(False, False)
    janela_lancar_solicitacao.iconbitmap(r"assets\icone_lancar.ico")
    janela_lancar_solicitacao.transient(janela)
    centralizar(janela_lancar_solicitacao)

    def fechar_janela():
        janela_lancar_solicitacao.destroy()
        button_lancar_solicitacao.config(state="normal")
    janela_lancar_solicitacao.protocol("WM_DELETE_WINDOW", fechar_janela)

    # SOLICITAÇÃO
    labelframe_solicitacao = ttk.LabelFrame(janela_lancar_solicitacao, text="Solicitação")
    labelframe_solicitacao.grid(row=0, column=0, padx=10, pady=(10, 0))
    entry_solicitacao = ttk.Entry(labelframe_solicitacao, width=10)
    entry_solicitacao.pack(side="left", padx=10, pady=10)
    
    # FINALIDADE
    labelframe_finalidade = ttk.LabelFrame(janela_lancar_solicitacao, text="Finalidade*")
    labelframe_finalidade.grid(row=0, column=1, padx=(2, 10), pady=(10, 0))
    combobox_finalidade = ttk.Combobox(labelframe_finalidade, width=15, values=["ADM. LOJAS", "ADM. CD", "REP. LOJAS", "REP. CD"], state="readonly")
    combobox_finalidade.pack(side="left", padx=10, pady=10)

    # EMPREGADO
    labelframe_empregado = ttk.Labelframe(janela_lancar_solicitacao, text="Empregado*")
    labelframe_empregado.grid(row=0, column=2, padx=(2, 10), pady=(10, 0))
    entry_empregado = ttk.Entry(labelframe_empregado, width=40)
    entry_empregado.pack(side="left", padx=10, pady=10)

    # CARGO
    labelframe_cargo = ttk.LabelFrame(janela_lancar_solicitacao, text="Cargo*")
    labelframe_cargo.grid(row=0, column=3, padx=(2, 10), pady=(10, 0))
    combobox_cargo = ttk.Combobox(labelframe_cargo, state="readonly", values=["CARGOS"])
    combobox_cargo.pack(side="left", padx=10, pady=10)

    # VESTUÁRIO
    labelframe_vestuario = ttk.Labelframe(janela_lancar_solicitacao, text="Vestuário*")
    labelframe_vestuario.grid(row=1, column=0, columnspan=4, padx=10, pady=(0, 10), sticky="ew")
    # -- ADICIONAR
    button_add = ttk.Button(labelframe_vestuario, text="+", width=2, command=lambda:adicionar_vestuario())
    button_add.grid(row=1, column=0, padx=10, pady=10)
    def adicionar_vestuario():
        linha_atual = labelframe_vestuario.grid_size()[1]
        # -- CATEGORIA
        combobox_categoria = ttk.Combobox(labelframe_vestuario, state="readonly", width=15, values=["UNIF. SUPERIOR", "UNIF. INFERIOR", "EPI - CALÇADO", "EPI - OUTRO"])
        combobox_categoria.grid(row=linha_atual, column=1, padx=(0, 10), pady=(0, 10), ipady=1)
        # -- PRODUTO
        combobox_produto = ttk.Combobox(labelframe_vestuario, state="readonly", width=50, values=["PRODUTO"])
        combobox_produto.grid(row=linha_atual, column=2, padx=(0, 10), pady=(0, 10), ipady=1)
        # -- TAMANHO
        entry_tamanho = ttk.Entry(labelframe_vestuario, width=10, justify="center")
        entry_tamanho.grid(row=linha_atual, column=3, padx=(0, 10), pady=(0, 10))
        # -- QUANTIDADE
        entry_quantidade = ttk.Entry(labelframe_vestuario, width=10, justify="center")
        entry_quantidade.grid(row=linha_atual, column=4, padx=(0, 10), pady=(0, 10))
        # -- REMOVER
        button_remove = ttk.Button(labelframe_vestuario,
                                   text="-",
                                   width=2,
                                   command=lambda linha_selecionada=linha_atual:remover_vestuario(linha_selecionada))
        button_remove.grid(row=linha_atual, column=5, padx=(0, 10), pady=(0, 10))
    # -- CATEGORIA
    label_categoria = ttk.Label(labelframe_vestuario, text="Categoria")
    label_categoria.grid(row=0, column=1, padx=(0, 10), pady=(10, 0))
    combobox_categoria = ttk.Combobox(labelframe_vestuario, state="readonly", width=15, values=["UNIF. SUPERIOR", "UNIF. INFERIOR", "CALÇADO", "OUTRO"])
    combobox_categoria.grid(row=1, column=1, padx=(0, 10), pady=10, ipady=1)
    # -- PRODUTO
    label_produto = ttk.Label(labelframe_vestuario, text="Produto")
    label_produto.grid(row=0, column=2, padx=(0, 10), pady=(10, 0))
    combobox_produto = ttk.Combobox(labelframe_vestuario, state="readonly", width=50, values=["PRODUTO"])
    combobox_produto.grid(row=1, column=2, padx=(0, 10), pady=10, ipady=1)
    # -- TAMANHO
    label_tamanho = ttk.Label(labelframe_vestuario, text="Tamanho")
    label_tamanho.grid(row=0, column=3, padx=(0, 10), pady=(10, 0))
    entry_tamanho = ttk.Entry(labelframe_vestuario, width=10, justify="center")
    entry_tamanho.grid(row=1, column=3, padx=(0, 10), pady=10)
    # -- QUANTIDADE
    label_quantidade = ttk.Label(labelframe_vestuario, text="Quantidade")
    label_quantidade.grid(row=0, column=4, padx=(0, 10), pady=(10, 0))
    entry_quantidade = ttk.Entry(labelframe_vestuario, width=10, justify="center")
    entry_quantidade.grid(row=1, column=4, padx=(0, 10), pady=10)
    # -- REMOVER
    button_remove = ttk.Button(labelframe_vestuario, text="-", width=2, command=lambda:remover_vestuario(1))
    button_remove.grid(row=1, column=5, padx=(0, 10), pady=10)
    def remover_vestuario(linha_selecionada):
        if linha_selecionada == 1:
            for widget in labelframe_vestuario.grid_slaves(row=linha_selecionada):
                    if isinstance(widget, ttk.Combobox):
                        widget.configure(state="normal")
                        widget.set("")
                        widget.configure(state="readonly")
                    elif isinstance(widget, ttk.Entry):
                        widget.delete(0, "end")
        else:
            for widget in labelframe_vestuario.grid_slaves(row=linha_selecionada):
                widget.destroy()
    # LANÇAR SOLICITAÇÃO
    button_lancar_solicitacao2 = ttk.Button(janela_lancar_solicitacao, text="Confirmar")
    button_lancar_solicitacao2.grid(row=2, column=0, columnspan=4, sticky="ew", padx=10, pady=(0, 10))

def centralizar(container):
    container.update_idletasks()
    x = (container.winfo_screenwidth() - container.winfo_width()) // 2
    y = (container.winfo_screenheight() - container.winfo_height()) // 2
    container.geometry(f"+{x}+{y}")
    container.geometry(f"+{x-148}+{y+8}")
janela.mainloop()