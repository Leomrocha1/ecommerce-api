# Ecommerce de Carros
Ecommerce de Carros

# Comandos para rodar projeto

### Criar o ambiente virtual
```
pip install virtualenv
```
```
virtualenv NomeDoAmbiente
```

### Ativar ambiente virtual

**Linux**
```
source NomeDoAmbiente/bin/activate
```

**Windows**
```
.\NomeDoAmbienteVirtual\Scripts\activate.bat
```
Caso o comando acima não funcione:
```
.\NomeDoAmbienteVirtual\Scripts\activate.ps1
```
Se tiver problemas com acesso não autorizado, utilize o seguinte comando no **powershell**:
```
Set-ExecutionPolicy Unrestricted -Scope Process
```


### Instalar dependências (necessário estar com ambiente virtual ativo)
```
pip install -r requitements.txt
```

### Rodar o projeto (necessário estar com ambiente virtual ativo)
```
python run.py
```
