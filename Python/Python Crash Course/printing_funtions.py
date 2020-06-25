#8.15 Printing Models

def print_models(unprinted_desings, completed_models):
    '''simula la impresion de cada diseno, hasta que no quede ninguno.
    luego mueve cada diseno a completed_models luego de haberlos imprimido
    '''
    while unprinted_desings:
        current_desings = unprinted_desings.pop()

        #simulate creating a 3D print from the desing.
        print("Printing model: " + current_desings)
        completed_models.append(current_desings)


def show_completed_models(completed_models):
    '''show all the models that were printed.'''
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_desings = ['iphone case', 'robot pendant', 'dragon toy']
completed_models = []

print_models(unprinted_desings, completed_models)
show_completed_models(completed_models)