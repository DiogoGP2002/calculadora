#include <stdio.h>

float soma(float a, float b){
    return a + b;
}

float subtracao(float a, float b){
    return a - b;
}

float divisao(float a, float b){
    if(b != 0){
        return a / b;
    }else{
        printf("ERRO: DIVISAO POR ZERO\n");
        return 0;
    }
}

float multiplicacao(float a, float b){
    return a * b;
}

int main(){
    float N1, N2, resultado;
    int Op;

    do{
        printf("\n======= [ CALCULADORA ] =======\n");
        printf("[1] SOMA\n");
        printf("[2] SUBTRACAO\n");
        printf("[3] DIVISAO\n");
        printf("[4] MULTIPLICACAO\n");
        printf("[0] SAIR\n");
        printf("Escolha: ");

        if(scanf("%d", &Op) != 1){
            printf("Entrada invalida!\n");
            return 1;
        }

        if(Op >= 1 && Op <= 4){
            printf("Digite o primeiro numero: ");
            if(scanf("%f", &N1) != 1){
                printf("Entrada invalida!\n");
                return 1;
            }

            printf("Digite o segundo numero: ");
            if(scanf("%f", &N2) != 1){
                printf("Entrada invalida!\n");
                return 1;
            }

            switch(Op){
                case 1:
                    resultado = soma(N1, N2);
                    printf("Resultado: %.2f\n", resultado);
                    break;
                case 2:
                    resultado = subtracao(N1, N2);
                    printf("Resultado: %.2f\n", resultado);
                    break;
                case 3:
                    resultado = divisao(N1, N2);
                    printf("Resultado: %.2f\n", resultado);
                    break;
                case 4:
                    resultado = multiplicacao(N1, N2);
                    printf("Resultado: %.2f\n", resultado);
                    break;
            }
        }

    }while(Op != 0);

    printf("Programa encerrado.\n");

    return 0;
}