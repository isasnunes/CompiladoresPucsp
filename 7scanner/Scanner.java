import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.regex.*;

/**
 * Scanner léxico para tokenizar textos em português.
 *
 * Entrada:
 *     Arquivo .txt (UTF-8)
 *
 * Saída:
 *     Arquivo output.txt (já existente), contendo um token por linha
 *
 * Disciplina: Compiladores - PUC-SP
 */
public class Scanner {

    /**
     * Método que realiza a tokenização usando regex
     */
    public static List<String> tokenizar(String texto) {

        List<String> tokens = new ArrayList<>();

        String regex =
                "\\.\\.\\." +                 // reticências
                "|\\d+(?:[.,]\\d+)?" +       // números
                "|[A-Za-zÀ-ÖØ-öø-ÿ]+(?:-[A-Za-zÀ-ÖØ-öø-ÿ]+)*" + // palavras
                "|[.,!?;:\"()\\[\\]—-]";     // pontuação

        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(texto);

        while (matcher.find()) {
            tokens.add(matcher.group());
        }

        return tokens;
    }

    public static void main(String[] args) {

        if (args.length < 1) {
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

            // mostrar exemplo
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

        } catch (IOException e) {
            System.out.println("Erro ao ler ou escrever arquivo: " + e.getMessage());
        }
    }
}