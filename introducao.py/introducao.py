#from kivy.app import App
#from kivy.uix.button import Button

#class MyApp(App):
 #   def build(self):
        # Cria um botão com o texto 'Hello, Kivy!'
  #      return Button(text='Hello, Kivy!')

#if __name__ == '__main__':
 #   MyApp().run()
#print("")

   #estrutura

print("Hello world")
#num =1
#num2 = 3
#soma = num + num2
#print(soma)

#string = input("digite o seu nome")
#print(string)
#print("Ola " +string+ ", seja-vindo a linguagem de programacao em python")

print ("1. Trabalhador\n"
       "2. estudante")

try:
    num = eval(input("digite a opcao: "))
    match num:
        case 1:
            print("Elisio")
        case 2:
            print("Leticia")
        case _:
            print("Error")
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")



    #Variaveis em python
    #e um espaco na memoria onde podemos armazenar dados
    #ex
