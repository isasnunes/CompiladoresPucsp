import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.regex.*;

/**
 * Disciplina: Compiladores - PUC-SP
 * Scanner léxico para tokenizar textos em português.
 *
 * Entrada:
 *     Arquivo .txt (UTF-8)
 *
 * Saída:
 *     Arquivo output.txt (já existente), contendo um token por linha
 */


/**
 * Método responsável pela tokenização do texto.
 *
 * Utiliza expressões regulares (regex) para identificar padrões
 * linguísticos e dividir o texto em tokens.
 *
 * @param texto Conteúdo completo do arquivo de entrada
 * @return Lista de tokens identificados no texto
 */
public class Scanner {
    public static List<String> tokenizar(String texto) {
        //Lista onde os tokens encontrados serão armazenados
        List<String> tokens = new ArrayList<>();

        String regex =
                "\\.\\.\\." +                 // reticências
                "|\\d+(?:[.,]\\d+)?" +       // números
                "|[A-Za-zÀ-ÖØ-öø-ÿ]+(?:-[A-Za-zÀ-ÖØ-öø-ÿ]+)*" + // palavras
                "|[.,!?;:\"()\\[\\]—-]";     // pontuação

        Pattern pattern = Pattern.compile(regex);    //compila a expressão regular em um padrão
        Matcher matcher = pattern.matcher(texto);    //cria um matcher para buscar padrões dentro do texto

        while (matcher.find()) {    //Percorre todo o texto procurando correspondências com a regex
            tokens.add(matcher.group());
        }

        return tokens;    //Retorna a lista de tokens encontrados
    }



    /**
     * Método principal do programa.
     *
     * Responsabilidades:
     * - Ler o arquivo de entrada informado via argumento
     * - Executar o scanner léxico
     * - Exibir alguns tokens no terminal
     * - Salvar todos os tokens no arquivo output.txt
     *
     * @param args Argumentos da linha de comando
     */
    public static void main(String[] args) {

        if (args.length < 1) {    //Verifica se o usuário forneceu o arquivo de entrada
            System.out.println("Uso: java Scanner <arquivo.txt>");
            return;
        }

        String arquivoEntrada = args[0];
        String arquivoSaida = "output.txt"; // já existe

        try {
            // leitura do arquivo
            String texto = Files.readString(Paths.get(arquivoEntrada));

            // tokenização
            List<String> tokens = tokenizar(texto);

            //exibe os primeiros 50 tokens no terminal
            System.out.println("Primeiros 50 tokens:");
            for (int i = 0; i < Math.min(50, tokens.size()); i++) {
                System.out.print(tokens.get(i) + " ");
            }

            // escrita no output.txt
            BufferedWriter writer = new BufferedWriter(new FileWriter(arquivoSaida));

            for (String token : tokens) {
                writer.write(token);
                writer.newLine();
            }

            writer.close();

            System.out.println("\n\nTotal de tokens: " + tokens.size());
            System.out.println("Tokens salvos em output.txt");

        } catch (IOException e) {    //Tratamento de erro
            System.out.println("Erro ao ler ou escrever arquivo: " + e.getMessage());
        }
    }
}
