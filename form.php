<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário</title>
</head>
<body>
    <h2>Formulário de Cadastro</h2>
    <form action="processar_formulario.php" method="POST">
        <label for="nome">Nome:</label><br>
        <input type="text" id="nome" name="nome"><br><br>
        
        <label for="numero">Número:</label><br>
        <input type="number" id="numero" name="numero"><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br><br>
        
        <label for="nota">Nota:</label><br>
        <input type="number" id="nota" name="nota"><br><br>
        
        <input type="submit" value="Enviar">
    </form>
</body>
</html>
