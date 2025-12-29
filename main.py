import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
linha_atual = 2

# JANELA
janela = tk.Tk()
janela.title("Controle de Uniformes e EPIs - Nome da Empresa")
janela.geometry("1080x720")
janela.resizable(False, False)
janela.configure(background="#f0f0f0")
janela.iconbitmap(r"assets\icone_app.ico")

# CENTRALIZA A JANELA
janela.withdraw()
x = (janela.winfo_screenwidth() - 1080) // 2
y = (janela.winfo_screenheight() - 720) // 2
janela.geometry(f"{1080}x{720}+{x}+{y}")
janela.deiconify()

# CONFIGURAÇÕES DE ESTILO
style = ttk.Style()
style.theme_use("vista")
style.configure("TNotebook.Tab",
                focuscolor="none",
                focusthickness=0,
                padding=5)

style.configure("TEntry",
                padding=5)

style.configure("TCombobox",
                padding=5)

style.configure("TButton",
                padding=5)

cor_chave = "#0078D7"

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
notebook.add(pagina_estoque, text="Estoque", image=img_estoque, compound="left")

# 01.1 CABEÇALHO
cabecalho = tk.Frame(pagina_estoque)
cabecalho.grid(row=0, column=0, sticky='ew')

img_estoque2 = tk.PhotoImage(file=r"assets\icone_estoque2.png")
tk.Label(cabecalho, image=img_estoque2).grid(row=0, column=0, rowspan=2)

titulo = ttk.Label(cabecalho, text="CONTROLE DE ESTOQUE", font=("Aptos", 20, "bold"), foreground=cor_chave)
titulo.grid(row=0, column=1, sticky="w", pady=(10, 0))

subtitulo = ttk.Label(cabecalho, text="Nome da Empresa", font=("Aptos", 9), foreground=cor_chave)
subtitulo.grid(row=1, column=1, sticky="w", pady=(0, 10))
# 01.2 LABELFRAME
filtros = tk.LabelFrame(pagina_estoque, text="Filtros")
filtros.grid(row=1, column=0, columnspan=2, pady=(0, 10), padx=(10, 0), sticky="ew")
# 01.2.1 BARRA DE BUSCA
label_produto = ttk.Label(filtros, text="Produto:")
label_produto.pack(fill="x", side="left", padx=10, pady=(5, 10))
entry_busca = ttk.Entry(filtros, width=37)
entry_busca.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
# 01.2.2 COMBOBOX
label_status = ttk.Label(filtros, text="Status:")
label_status.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
combobox_status = ttk.Combobox(filtros, values=["ESTOQUE EXCESSIVO", "ESTOQUE ADEQUADO", "ESTOQUE MÍNIMO", "ESTOQUE ZERADO"], state="readonly", width=37)
combobox_status.pack(fill="x", side="left", padx=(0, 10), pady=(5, 10))
# 01.2.2 BOTÃO BUSCAR
button_buscar = ttk.Button(filtros, text="Buscar", width=20)
button_buscar.pack(fill="x", side="right", padx=(0, 10), pady=(5, 10))
# 01.3 TABELA ESTOQUE
tabela_estoque = ttk.Treeview(pagina_estoque, columns=("ID", "Produto", "Disponível", "Pendente", "Status"), show="headings", height=24)
tabela_estoque.heading("ID", text="ID")
tabela_estoque.column("ID", width=20, anchor="center")
tabela_estoque.heading("Produto", text="Produto")
tabela_estoque.column("Produto", width=400, anchor="center")
tabela_estoque.heading("Disponível", text="Disponível")
tabela_estoque.column("Disponível", width=100, anchor="center")
tabela_estoque.heading("Pendente", text="Pendente")
tabela_estoque.column("Pendente", width=100, anchor="center")
tabela_estoque.heading("Status", text="Status")
tabela_estoque.column("Status", width=120, anchor="center")
tabela_estoque.grid(row=2, column=0, columnspan=2, padx=(10, 0), sticky="ew")

# ==============================================================================
# 02. PÁGINA SOLICITAÇÕES DO NOTEBOOK
# ==============================================================================
img_solicitacoes = tk.PhotoImage(file=r"assets\icone_solicitacoes.png")
pagina_solicitacoes = ttk.Frame(notebook)
notebook.add(pagina_solicitacoes, text="Solicitações", image=img_solicitacoes, compound="left")

# ==============================================================================
# 03. PÁGINA DASHBOARDS DO NOTEBOOK
# ==============================================================================
img_dashboard = tk.PhotoImage(file=r"assets\icone_dashboard.png")
pagina_dashboards = ttk.Frame(notebook)
notebook.add(pagina_dashboards, text="Dashboards", image=img_dashboard, compound="left")

# ==============================================================================
# 04. PÁGINA PRODUTOS
# ==============================================================================
img_produtos = tk.PhotoImage(file=r"assets\icone_produtos.png")
pagina_produtos = ttk.Frame(notebook)
notebook.add(pagina_produtos, text="Produtos", image=img_produtos, compound="left")

# ==============================================================================
# 05. PÁGINA FORNECEDORES
# ==============================================================================
img_fornecedores = tk.PhotoImage(file=r"assets\icone_fornecedores.png")
pagina_fornecedores = ttk.Frame(notebook)
notebook.add(pagina_fornecedores, text="Fornecedores", image=img_fornecedores, compound="left")

# ==============================================================================
# 06. PÁGINA UNIDADES
# ==============================================================================
img_unidades = tk.PhotoImage(file=r"assets\icone_unidades.png")
pagina_unidades = ttk.Frame(notebook)
notebook.add(pagina_unidades, text="Unidades", image=img_unidades, compound="left")

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
logo_texto = ttk.Label(barra_lateral, text="- CONTROLE -\nUNIFORMES E EPIS", font=("Aptos", 16, "bold"), foreground="#FFFFFF", background=cor_chave, justify="center")
logo_texto.pack(pady=(20, 0))
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
button_relatorio = ttk.Button(barra_lateral, text="Exportar Relatório", width=25)
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

unidades = []
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
    button_lancar_transacao2 = ttk.Button(janela_lancar_transacao, text="Lançar", command=lambda:lancar_transacao())
    button_lancar_transacao2.grid(row=1, column=2, padx=(2, 10), pady=10, sticky="wens")
    def lancar_transacao():
        print()

solicitacoes = []
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
    combobox_finalidade = ttk.Combobox(labelframe_finalidade, width=15, values=["ADM. KRILL", "ADM. MAZZINI", "REP. KRILL", "REP. MAZZINI"], state="readonly")
    combobox_finalidade.pack(side="left", padx=10, pady=10)

    # NOME
    labelframe_nome = ttk.Labelframe(janela_lancar_solicitacao, text="Nome*")
    labelframe_nome.grid(row=0, column=2, padx=(2, 10), pady=(10, 0))
    entry_nome = ttk.Entry(labelframe_nome, width=40)
    entry_nome.pack(side="left", padx=10, pady=10)

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
        combobox_categoria = ttk.Combobox(labelframe_vestuario, state="readonly", width=15, values=["UNIF. SUPERIOR", "UNIF. INFERIOR", "CALÇADO", "OUTRO"])
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
    button_lancar_solicitacao2 = ttk.Button(janela_lancar_solicitacao, text="Lançar Solicitação")
    button_lancar_solicitacao2.grid(row=2, column=0, columnspan=4, sticky="ew", padx=10, pady=(0, 10))

def centralizar(container):
    container.update_idletasks()
    x = (container.winfo_screenwidth() - container.winfo_width()) // 2
    y = (container.winfo_screenheight() - container.winfo_height()) // 2
    container.geometry(f"+{x}+{y}")
    container.geometry(f"+{x-148}+{y+8}")
janela.mainloop()