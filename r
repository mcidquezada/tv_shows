shows

show1 = Shows.objects.create(title = "Stranger Things", network = "Netflix", date="", description="Niños que viven cosas extrañas")
show2 = Shows.objects.create(title = "Bronklyn Nine-Nine", network = "NBC", date="", description="Los detectives Jake Peralta, Amy Santiago, Rosa Diaz y la sargento Terry Jeffords son unos policías talentosos, sin preocupaciones y con el mejor registro de arrestos, hasta que llega a la estación policial el nuevo jefe Raymond Holt.")
show3 = Shows.objects.create(title= "Game of Throne" , network="HBO", date = " ", description ="Familias que se matan unas a otras" )
show = Shows.objects.all()