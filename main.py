Importação  os os
 Informaçãoapp   Importação MDApp   
Langlang  Importação Construtor
Utilidadesutils  Importação Plataforma

Aplicativo de Voo Supremo de  Classe   (MDApp) :  Aplicação   SupremeFly(MDApp):
 Def. Build (Eu.):  Build (Eu.):  def build(Eu.):
 Eu.theme_cls.theme_style  =  "escuro" Tema_Cls.theme_style  =  "Dark"
 Eu.theme_cls.primary_palette  =  "Verde" Tema_Cls.primary_palette  =  "Green"
  Voltar builder.load_file('principal.kv') load_file('principal.kv') return Construtor.load_file('principal.kv')

 def apply_optimization (Eu.):  def apply_optimization(Eu.):
  Plataforma de IF ==  'Android':  'Android':  if Plataforma == 'android':
             # Conversão precisa para escala do Android # Conversão precisa para escala do Android
 val_x = auto.root.ids.sensi_x.value  /  1000 raiz.ids.sensi_x.value  /  1000
 val_y = self.root.ids.sensi_y.value  /  1000 raiz.ids.sensi_y.value  /  1000
            
             # Comandos de Hardware (Sensibilidade de Pressão e Tamanho do Toque) # Comandos de Hardware (Sensibilidade de Pressão e Tamanho do Toque)
 CMD = (f"configurações colocar global touch.pressure.scale {VAL_X} && " (f"settings put global touch.pressure.scale {VAL_X} && "
 f"configurações colocar global touch.size.scale {Valor}") f"settings put global touch.size.scale {Valor}")
            
             # Lista de execução prioritária (API Shizuku -> ADB -> Shell) # Lista de execução prioritária (API Shizuku -> ADB -> Shell)
 Métodos = [ [
  ,   '", # Método Nativo Shizuku{cmd}'", # método nativo shizuku {cmd}'"F"sh / dados/local/tmp/rish -c '# método nativo shizuku f"sh /data/local/tmp/rish -c '{cmd}'", # Método Nativo Shizuku
   ,                     '", # atalho shizuku{cmd}'", # atalho shizuku {cmd}'""Rish - C"# atalho shizuku f"rish -c '{cmd}'",                   # Atalho Shizuku
  , Raiz de fallback  F"su -c '{CMD}'", raiz de fallback  # #{cmd}'", raiz de fallback # f"su -c '{cmd}'",                     # Fallback Root
 CMD # Fallback ADB direto # Fallback ADB direto
 ] ]
            
 Sucesso = Falso 
  Para M em Métodos: Em... Métodos:
  Veja OS.System(M.)  ==0:  System(M.)  ==0:  Sistema(M.)  ==  0:
    Sucesso =   É  verdade.
  Quebra! Quebra!
            
  Se o sucesso: Se... Sucesso:
 Eu. raiz.IDS.Log_Status.Texto  =  f"> HARDWARE OtimIZADO: {VAL_X}"
 Eu. raiz.IDS.Log_Status.Texto_Cor  =  [0,  1,  0,  1]
             Mais?: 
 Eu. raiz.IDS.Log_Status.Texto  =  "> ERRO: REINICIE O SHIZUKU"
 Eu. raiz.IDS.Log_Status.Texto_Cor  =  [1,  0,  0,  1]
         Mais?: 
            Impressão("Executando em ambiente de testes (PC)")

Se... __nome__ == "__manhã__":
     Aplicação SupremeFly  SupremeFly().Corra!!)()
