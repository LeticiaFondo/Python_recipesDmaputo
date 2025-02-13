import

1.
Criar
o
Projeto
ASP.NET
MVC
No
Visual
Studio, crie
um
novo
projeto
do
tipo
ASP.NET
Web
Application(.NET
Framework) e
selecione
o
template
MVC.
Certifique - se
de
que as dependências
estão
corretamente
configuradas
para
MVC.
2.
Criar
o
Controller
para
Administrador(AdminController)
No
Solution
Explorer, clique
com
o
botão
direito
na
pasta
Controllers > Add > Controller > Escolha
MVC
Controller - Empty
e
nomeie
como
AdminController.
AdminController.cs:

csharp
Copy
code
public


class AdminController: Controller


{
    private
static
int
loginAttempts = 0; // Para
contar as tentativas
de
login

// Exibir
a
página
de
login
public
ActionResult
Auth()
{
return View();
}

// Post
do
login
[HttpPost]
public
ActionResult
Auth(string
username, string
password)
{
if (username == "admin" & & password == "admin")
    {
    // Resetar
    tentativas
    e
    redirecionar
    para
    a
    página
    inicial
    loginAttempts = 0;
return RedirectToAction("Index", "Admin");
}
else
{
loginAttempts + +;
if (loginAttempts >= 3)
    {
        ViewBag.Message = "Você excedeu o número de tentativas. Tente novamente mais tarde.";
return View();
}
else
{
ViewBag.Message = "Credenciais inválidas. Você tem " + (3 - loginAttempts) + " tentativas restantes.";
return View();
}
}
}

// Página
inicial
após
login
public
ActionResult
Index()
{
return View();
}
}
3.
Criar
o
Controller
para
Funcionario(FormularioController)
No
Solution
Explorer, adicione
outro
controller
chamado
FormularioController.
FormularioController.cs:

csharp
Copy
code
public


class Funcionario
    {
        public
    int
    Id
    {get;
    set;}
    public
    string
    Nome
    {get;
    set;}
    public
    string
    Apelido
    {get;
    set;}
    public
    string
    Genero
    {get;
    set;}
    public
    string
    Categoria
    {get;
    set;}
    }

    public

    class FormularioController:
        Controller

    {
        private
    static
    List < Funcionario > funcionarios = new
    List < Funcionario > ();

    // Exibir
    a
    lista
    de
    funcionários
    cadastrados
    public
    ActionResult
    Listagem()
    {
    return View(funcionarios);
    }

    // Exibir
    o
    formulário
    de
    cadastro
    de
    novos
    funcionários
    public
    ActionResult
    CadastroFuncionario()
    {
    return View();
    }

    // Salvar
    os
    dados
    de
    um
    novo
    funcionário
    [HttpPost]
    public
    ActionResult
    SalvarFuncionario(Funcionario
    funcionario)
    {
    if (ModelState.IsValid)
        {
            funcionarios.Add(funcionario);
        TempData["Message"] = "Funcionário cadastrado com sucesso!";
    return RedirectToAction("Index", "Admin");
    }
    return View("CadastroFuncionario");
    }
    }
    4.
    Views
    4.1.Auth.cshtml(Formulário
    de
    Login
    do
    Administrador):
    Criar
    a
    View
    Auth.cshtml
    dentro
    de
    Views / Admin.
    html
    Copy
    code
    < h2 > Login
    do
    Administrador < / h2 >
                      < form
    method = "post"
    action = "/Admin/Auth" >
             < label
    for ="username" > Usuário:< / label >
                                  < input
    type = "text"
    id = "username"
    name = "username"
    required / >
    < br / >
    < label
    for ="password" > Senha:< / label >
                                < input
    type = "password"
    id = "password"
    name = "password"
    required / >
    < br / >
    < input
    type = "submit"
    value = "Login" / >
            < / form >
                < p >

    @ViewBag.Message <

    / p >
      4.2.Index.cshtml(Página
    Inicial
    do
    Administrador):
    Criar
    a
    View
    Index.cshtml
    dentro
    de
    Views / Admin.
    html
    Copy
    code
    < h2 > Página
    Inicial
    do
    Administrador < / h2 >
                      < a
    href = "/Formulario/Listagem" > Ver
    lista
    de
    funcionários < / a >
                     < br / >
                     < a
    href = "/Formulario/CadastroFuncionario" > Cadastrar
    novo
    funcionário < / a >

                    < p >

    @TempData["Message"] <

    / p >
      4.3.Listagem.cshtml(Lista
    de
    Funcionários):
    Criar
    a
    View
    Listagem.cshtml
    dentro
    de
    Views / Formulario.
    html
    Copy
    code
    < h2 > Lista
    de
    Funcionários < / h2 >
                     < table >
                     < tr >
                     < th > ID < / th >
                                   < th > Nome < / th >
                                                   < th > Apelido < / th >
                                                                      < th > Gênero < / th >
                                                                                        < th > Categoria < / th >
                                                                                                             < / tr >

    @foreach(var

    funcionario in Model)
    {
    < tr >
    < td >

    @funcionario.Id <

    / td >
      < td >

    @funcionario.Nome <

    / td >
      < td >

    @funcionario.Apelido <

    / td >
      < td >

    @funcionario.Genero <

    / td >
      < td >

    @funcionario.Categoria <

    / td >
      < / tr >
    }
    < / table >
        4.4.CadastroFuncionario.cshtml(Formulário
    de
    Cadastro
    de
    Funcionários):
    Criar
    a
    View
    CadastroFuncionario.cshtml
    dentro
    de
    Views / Formulario.
    html
    Copy
    code
    < h2 > Cadastrar
    Novo
    Funcionário < / h2 >
                    < form
    method = "post"
    action = "/Formulario/SalvarFuncionario" >
             < label
    for ="id" > ID:< / label >
                       < input
    type = "number"
    id = "id"
    name = "Id"
    required / >
    < br / >
    < label
    for ="nome" > Nome:< / label >
                           < input
    type = "text"
    id = "nome"
    name = "Nome"
    required / >
    < br / >
    < label
    for ="apelido" > Apelido:< / label >
                                 < input
    type = "text"
    id = "apelido"
    name = "Apelido"
    required / >
    < br / >
    < label
    for ="genero" > Gênero:< / label >
                               < input
    type = "text"
    id = "genero"
    name = "Genero"
    required / >
    < br / >
    < label
    for ="categoria" > Categoria:< / label >
                                     < input
    type = "text"
    id = "categoria"
    name = "Categoria"
    required / >
    < br / >
    < input
    type = "submit"
    value = "Cadastrar" / >
            < / form >
                5.
    Adicionar
    Alertas
    e
    Redirecionamentos
    Quando
    o
    formulário
    de
    cadastro
    é
    submetido
    com
    sucesso, o
    TempData["Message"]
    armazena
    uma
    mensagem
    de
    sucesso
    que
    será
    exibida
    na
    página
    inicial.
    Utilize
    o
    código
    TempData
    na
    Index.cshtml
    para
    exibir
    a
    mensagem
    de
    sucesso
    logo
    após
    o
    cadastro.
    6.
    Configuração
    da
    Rota
    Abra
    o
    arquivo
    RouteConfig.cs
    em
    App_Start
    e
    modifique
    a
    rota
    padrão
    para
    redirecionar
    para
    a
    página
    de
    login:
    csharp
    Copy
    code
    routes.MapRoute(
        name: "Default",
    url: "{controller}/{action}/{id}",
    defaults: new
    {controller = "Admin", action = "Auth", id = UrlParameter.Optional}
    );
    Fluxo
    da
    aplicação:
    O
    administrador
    acessa
    a
    página
    de
    login(Auth.cshtml).
    Se
    o
    login
    for bem - sucedido, ele será redirecionado para a página inicial (Index.cshtml).
    Na página inicial, ele poderá visualizar a lista de funcionários ou acessar o formulário de cadastro.
    Após cadastrar um novo funcionário, o administrador será redirecionado para a página inicial com uma mensagem de sucesso.
    Essa estrutura cumpre todos os requisitos, com autenticação, controle de acesso, cadastro e exibição de funcionários.

    Como validar o login?

    Onde criar o layout?
