import graphene
from graphene_django import DjangoObjectType
from .models import Cliente

#Serializar datos de cliente
class ClienteType(DjangoObjectType):
    class Meta:
        model = Cliente
        fields = '__all__'

#Listar clientes
class Query(graphene.ObjectType):
    clientes = graphene.List(ClienteType)

    def resolve_clientes(self, info, **kwargs):
        return Cliente.objects.all()
    
    def resolve_clientes_by_uid(self, info, uid):
        return Cliente.objects.get(uid=uid)

#Mutacion para crear un cliente
class CreateClienteMutation(graphene.Mutation):
    class Arguments:
        uid = graphene.String()
        nombre = graphene.String()
        apellido = graphene.String()
        direccion = graphene.String()
        telefono = graphene.String()
        email = graphene.String()

    cliente = graphene.Field(ClienteType)

    def mutate(self, info, uid, nombre, apellido, direccion, telefono, email):
        cliente = Cliente(uid=uid, nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono, email=email)
        cliente.save()
        return CreateClienteMutation(cliente=cliente)

#Mutacion para actualizar un cliente
class UpdateClienteMutation(graphene.Mutation):
    class Arguments:
        uid = graphene.String()
        nombre = graphene.String()
        apellido = graphene.String()
        direccion = graphene.String()
        telefono = graphene.String()
        email = graphene.String()

    cliente = graphene.Field(ClienteType)

    def mutate(self, info, uid, **kwargs):
        cliente = Cliente.objects.get(uid=uid)
        for field,value in kwargs.items():
            setattr(cliente,field,value)
        cliente.save()
        return UpdateClienteMutation(cliente=cliente)

#Mutacion para eliminar un cliente
class DeleteClienteMutation(graphene.Mutation):
    class Arguments:
        uid = graphene.String()

    cliente = graphene.Field(ClienteType)

    def mutate(self, info, uid):
        cliente = Cliente.objects.get(uid=uid)
        cliente.delete()
        return DeleteClienteMutation(cliente=cliente)

#Las mutaciones creadas deben añadirse aca
class Mutation(graphene.ObjectType):
    create_cliente = CreateClienteMutation.Field()
    update_cliente = UpdateClienteMutation.Field()
    delete_cliente = DeleteClienteMutation.Field()
    
#Mutaciones, consultas y demas debe registrarse aqui
schema = graphene.Schema(query=Query,mutation=Mutation)
