Algoritmo "AnaliseDeDados"
// ==========================================
// Equivalência de Regex e Tratamento de Exceções
// ==========================================
Var
   nomes: vetor[1..2] de caractere
   cpfs: vetor[1..2] de caractere
   
   i, registros_validos, registros_invalidos: inteiro
   
   // Variáveis para "simular" as exceções
   deu_erro: logico
   mensagem_erro: caractere

Inicio
   // Simulando a leitura de um arquivo CSV colocando dados nos vetores
   // Registro 1: Certo
   nomes[1] <- "Ana"
   cpfs[1] <- "111.222.333-44"
   
   // Registro 2: Errado (Sem os pontos e traço)
   nomes[2] <- "Carlos"
   cpfs[2] <- "22233344455"
   
   registros_validos <- 0
   registros_invalidos <- 0
   
   Escreval("Iniciando analise de dados...")
   Escreval("")
   
   Para i de 1 ate 2 faca
      deu_erro <- falso
      
      // ==========================================
      // SIMULANDO EXPRESSÕES REGULARES (REGEX)
      // Como não existe Regex no Portugol, verificamos o tamanho da String
      // Um CPF com pontuação deve ter exatamente 14 caracteres.
      // ==========================================
      Se (Compr((cpfs[i])) <> 14) Entao
         // ==========================================
         // SIMULANDO A EXCEÇÃO (Raise FormatoInvalidoError)
         // ==========================================
         deu_erro <- verdadeiro
         mensagem_erro <- "Formato de CPF invalido! Faltam pontos ou tracos."
      FimSe
      
      // ==========================================
      // SIMULANDO O TRY / EXCEPT
      // Se deu_erro for verdadeiro, ele cai no 'Except'
      // ==========================================
      Se (deu_erro = verdadeiro) Entao
         registros_invalidos <- registros_invalidos + 1
         Escreval("⚠️ ERRO na Linha ", i, " (", nomes[i], "): ", mensagem_erro)
      Senao
         // Se não deu erro, cai no nosso 'Else' do Try
         registros_validos <- registros_validos + 1
      FimSe
      
   FimPara
   
   // ==========================================
   // SIMULANDO O BLOCO FINALLY E RELATÓRIO
   // ==========================================
   Escreval("")
   Escreval("========================================")
   Escreval("📊 RELATORIO FINAL")
   Escreval("========================================")
   Escreval("Registros Validos: ", registros_validos)
   Escreval("Registros Invalidos: ", registros_invalidos)
   Escreval("========================================")
   Escreval("Fim do processo. Fechando conexoes...")
   
Fimalgoritmo