''' Crear calculadora con los diferentes indicadores
de estado fisico (peso, grasa, calorias, entre otros)
  ->  Calcular el peso ideal (IBW)
      • Hombre = 56.2 +1.41*(Altura (cm)/2.54 -60)
      • Mujer = 53.1 +1.36 *(Altura (cm)/2.54 -60))
  ->  Calorias Quemadas
      • Calorías quemadas = (Tiempo actividad (min) * MET * Peso(Kg)) /200
      Valores del MET
        • Caminar = 2
        • Tenis = 5
        • Montar en bicicleta = 14
        • Correr = 6
        • Nadar = 9.8
  -> PORCENTAJE DE GRASA CORPORAL
      • Hombres adultos = 1.20 * IMC + 0.23 * Edad - 16.2
      • Mujeres adultas = 1.20 * IMC + 0.23 * Edad - 5.4
      - IMC = peso (Kg) / Altura2 (m)
  -> ÍNDICE METABÓLICO BASAL
      • Hombres = 13.397P + 4.799E - 5.677A + 88.362
      • Mujeres = 9.247P + 3.098E - 4.330A + 447.593

      • P = Peso en Kg
      • A = Altura en cm
      • E = Edad en años

--> RETO: Realizar una aplicación que permita calcular todas las métricas de la calculadora saludable (para hombres y mujeres) utilizando todos los pasos del método IDEAL.
<--
'''
#definimos funciones
def calculoPesoIdeal (altura):
  IBWHombre = 56.2 + 1.41*(altura/2.54 -60)
  IBWMujer = 53.1 + 1.36*(altura/2.54 -60)
  return(print("-> El peso ideal (IBW) del Hombre es: ", IBWHombre, "\n-> El peso ideal (IBW) de la Mujer es: ", IBWMujer, "\n"))

def caloriasQuemadas (tiempoActividad, valorMET, peso):
  calQuemadas = tiempoActividad * valorMET * peso / 200
  return(print("-> Las Calorias Quemadas fueron:", calQuemadas, "\n"))
  
def porcentajeGrasaCorporal (peso, altura, edad):
  IMC = peso / altura**2
  homAdultos = 1.20 * IMC + 0.23 * edad - 16.2
  mujAdultas = 1.20 * IMC + 0.23 * edad - 5.4
  return(print("-> El Porcentaje de Grasa Corporal en un Hombre Adulto es: ", homAdultos, "-> El Porcentaje de Grasa Corporal en una Mujer Adulta es: ", mujAdultas, "\n"))

def tasaMetabolicaBasal (peso, altura, edad):
  TMBhombre = ((13.397*peso) + (4.799*edad) - (5.677*altura) + 88.362)
  TMBmujeres = ((9.247*peso) + (3.098*edad) - (4.330*altura) + 447.593)
  return(print("-> La Tasa Metabolica Basal en un Hombre Adulto es: ", TMBhombre, "\n -> La Tasa Metabolica Basal en una Mujer Adulta es: ", TMBmujeres, "\n"))

#pedimos los datos que el usuario va a ingresar y se guardan en las variables
altura = float(input("Ingresa su Altura en Centimetros: "))
tiempoActividad = float(input("Ingresa su tiempo de actividad en Minutos: "))
valorMET = float(input("Ingresa su valor del MET, Valores -> Caminar = 2, Tenis = 5, Montar en bicicleta = 14, Correr = 6, Nadar = 9.8 \n"))
peso = float(input("Ingresa su Peso en Kilogramos: "))
edad = float(input("Ingresa su Edad en años: "))
print("\n")

#Llamo las funciones
calculoPesoIdeal(altura)
caloriasQuemadas(tiempoActividad, valorMET, peso)
porcentajeGrasaCorporal (peso, altura, edad)
tasaMetabolicaBasal (peso, altura, edad)