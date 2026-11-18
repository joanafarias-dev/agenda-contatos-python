import json

try:
	with open("contatos.json", "r", encoding="utf-8") as arquivo:
		agenda=json.load(arquivo)
except FileNotFoundError:
	agenda=[]

def salvar_contatos():
	with open("contatos.json", "w", encoding="utf-8") as arquivo:
		json.dump(agenda, arquivo, ensure_ascii=False, indent=4)
		
while True: 
	print("\n------Agenda de contatos-----\n")
	opcao= input(" Digite: 1 - adicionar contatos, 2 - ver lista de contatos, 3 - excluir contato , 4 - sair: ")
	if opcao == "1":
		nome= input("Digite o nome: ").strip().lower()
		telefone =input("Digite o telefone: ")
		contato = {"nome": nome, "telefone": telefone}
		agenda.append(contato)
		salvar_contatos()
		print()
	elif opcao == "2":
		if agenda:
			for contato in agenda:
				print(contato["nome"], contato["telefone"])
			print()
		else:
			print("Nenhum contato cadastrado\n")
	elif opcao == "3":
		while True:
			nome_exclusao= input("Digite o nome do contato que deseja excluir (ou 0 para voltar): ").strip().lower()
			encontrado= False
			for contato in agenda:
				if nome_exclusao== contato["nome"]:
					agenda.remove(contato)
					salvar_contatos()
					encontrado= True
					print("Contato excluido com sucesso. \n")
					break
			if encontrado:
				break
			elif nome_exclusao =="0":
				break
			else:
				print("Contato nao encontrado.\n")
	elif opcao == "4":
		print("\nOk, bye!\n")
		break
	else:
		print("Opcao invalida")