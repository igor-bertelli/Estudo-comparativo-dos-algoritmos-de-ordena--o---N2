#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <stack>

using namespace std;

// Função para trocar dois elementos
void swap(int& a, int& b, int& trocas) {
    int temp = a;
    a = b;
    b = temp;
    trocas++;
}

// Função para encontrar o pivô e colocar os elementos menores à esquerda e os maiores à direita
int partition(vector<int>& arr, int low, int high, int& trocas, int& comparacoes) {
    int pivot = arr[high]; // Escolhe o último elemento como pivô
    int i = low - 1; // Índice do menor elemento

    for (int j = low; j <= high - 1; j++) {
        comparacoes++;
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j], trocas);
        }
    }

    swap(arr[i + 1], arr[high], trocas);
    return i + 1;
}

// Função principal do Quick Sort (versão iterativa)
void quickSort(vector<int>& arr, int low, int high, int& trocas, int& comparacoes) {
    stack<pair<int, int>> pilha; // Pares (low, high) a serem processados

    pilha.push({low, high});

    while (!pilha.empty()) {
        pair<int, int> intervalo = pilha.top();
        pilha.pop();

        low = intervalo.first;
        high = intervalo.second;

        if (low < high) {
            int pi = partition(arr, low, high, trocas, comparacoes);

            // Recurso no lado mais curto primeiro
            if (pi - low < high - pi) {
                pilha.push({low, pi - 1});
                pilha.push({pi + 1, high});
            } else {
                pilha.push({pi + 1, high});
                pilha.push({low, pi - 1});
            }
        }
    }
}

// Função para inicializar o Quick Sort
void performQuickSort(vector<int>& arr, int& trocas, int& comparacoes) {
    int low = 0;
    int high = arr.size() - 1;
    trocas = 0;
    comparacoes = 0;
    quickSort(arr, low, high, trocas, comparacoes);
}

int main() {
    srand(static_cast<unsigned>(time(0)));

    // Tamanhos dos vetores
    vector<int> tamanhos = {1000, 10000, 100000};

    for (int tamanho : tamanhos) {
        vector<int> vetorMelhorCaso(tamanho);
        vector<int> vetorCasoMedio(tamanho);
        vector<int> vetorPiorCaso(tamanho);

        // Preencher vetores para os casos
        for (int i = 0; i < tamanho; i++) {
            vetorMelhorCaso[i] = i;
            vetorCasoMedio[i] = rand() % tamanho;
            vetorPiorCaso[i] = tamanho - i;
        }

        // Medir o tempo de execução, quantidade de trocas e comparações para o Melhor Caso
        clock_t startMelhorCaso = clock();
        int trocasMelhorCaso, comparacoesMelhorCaso;
        performQuickSort(vetorMelhorCaso, trocasMelhorCaso, comparacoesMelhorCaso);
        clock_t endMelhorCaso = clock();
        double tempoMelhorCaso = static_cast<double>(endMelhorCaso - startMelhorCaso) / CLOCKS_PER_SEC;

        // Medir o tempo de execução, quantidade de trocas e comparações para o Caso Médio
        clock_t startCasoMedio = clock();
        int trocasCasoMedio, comparacoesCasoMedio;
        performQuickSort(vetorCasoMedio, trocasCasoMedio, comparacoesCasoMedio);
        clock_t endCasoMedio = clock();
        double tempoCasoMedio = static_cast<double>(endCasoMedio - startCasoMedio) / CLOCKS_PER_SEC;

        // Medir o tempo de execução, quantidade de trocas e comparações para o Pior Caso
        clock_t startPiorCaso = clock();
        int trocasPiorCaso, comparacoesPiorCaso;
        performQuickSort(vetorPiorCaso, trocasPiorCaso, comparacoesPiorCaso);
        clock_t endPiorCaso = clock();
        double tempoPiorCaso = static_cast<double>(endPiorCaso - startPiorCaso) / CLOCKS_PER_SEC;

        // Exibir resultados
        cout << "Tamanho do vetor: " << tamanho << endl;
        cout << "Melhor Caso:" << endl;
        cout << "Tempo de Execucao: " << tempoMelhorCaso << " segundos" << endl;
        cout << "Quantidade de Trocas: " << trocasMelhorCaso << endl;
        cout << "Quantidade de Comparacoes: " << comparacoesMelhorCaso << endl;

        cout << "Caso Medio:" << endl;
        cout << "Tempo de Execucao: " << tempoCasoMedio << " segundos" << endl;
        cout << "Quantidade de Trocas: " << trocasCasoMedio << endl;
        cout << "Quantidade de Comparacoes: " << comparacoesCasoMedio << endl;

        cout << "Pior Caso:" << endl;
        cout << "Tempo de Execucao: " << tempoPiorCaso << " segundos" << endl;
        cout << "Quantidade de Trocas: " << trocasPiorCaso << endl;
        cout << "Quantidade de Comparacoes: " << comparacoesPiorCaso << endl;

        cout << "----------------------------------------" << endl;
    }

    return 0;
}
