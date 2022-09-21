
//PROJECTE DE BDNR//
//Consultes - joc de proves de la nostra BD//
//Joel Soler Huix - 1531139//
//Gerard Santacatalina Rubio - 1534002//

//Consulta 1 
db.autors.aggregate([
    {$match: {Extranjero: true, Autor: {$not:{$in:['Anonimo', 'Anonimo - traducciones']}}}},
    {$unwind:"$Contes"},
    {$project: {Contes: 1, Autor: 1, _id: 0}},
    {$sort: {Autor: 1}}])
    
//Consulta 2


db.cuentos.aggregate([
    {$unwind:"$temas"},
    {$match:{$or:[{temas: 'Matrimonio forzoso'}, {temas: 'Matrimonios forzosos'}]}},
    {$project:{_id:0, temas:1, titulo:1}}])
    
//Consulta 3

var x = db.autors.find({$or:[{Autor: 'Sánchez Viedma, José'}, {Autor: 'Sanchez Biedma, Jose'}]}).toArray()
db.cuentos.aggregate([
    {$match:{$or:[{titulo:x[0]["Contes"][0]}, {titulo: x[0]["Contes"][1]}]}},
    {$project:{'titulo': 1, revista:{$slice: ['$publicaciones.revista', 1]}, data:{$slice:['$publicaciones.data',1]}, pagines:{$slice:['$publicaciones.pagines',1]}, '_id':0}}])
    
//Consulta 4
db.autors.aggregate([
    {$match:{Autor:{$not:{$in:['Anonimo', 'Anonimo - traducciones']}}}},
    {$addFields:{"Cont":{$size:"$Contes"}}},
    {$sort:{Cont:-1}},
    {$limit:1},
    {$project:{Autor:1, Extranjero:1, Cont:1, _id:0}}
    ])


//Consulta 6
//Dues maneres:

//Fent servir el find:
db.cuentos.find({"publicaciones.data":{'$gte':ISODate('1840-01-01'), '$lte':ISODate('1850-01-01')}}).count()

//Amb un aggregate:
db.cuentos.aggregate([
    {$match:{"publicaciones.data":{'$gte':ISODate('1840-01-01'), '$lte':ISODate('1850-01-01')}}},
    {$count:"Nombre_contes"}])


  
