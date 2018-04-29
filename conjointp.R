###profile
#profile1:	average    VS	 	bralette
#profile2:	low 		Aerie 	bralette
#profile3:	high    	CK 		bralette
#profile4:	average    	CK   		sports
#profile5:	high 		VS   	sports
#profile6:	low    Aerie   		sports
#profile7:	high    	CK    	sports
#profile8:	high 		VS    	laced
#profile9:	average    	Aerie    	laced
#profile10:	high    CK    	laced
#profile11:	high    	VS   		pushup
#profile12:	average 	Aerie   	pushup
#profile13:	average    	CK   		pushup
###

library("AlgDesign") # install.packages("AlgDesign") if necessary.
candidate.list = expand.grid(price = c("low", "average", "high"),
  brand = c("VS", "Aerie", "CK"),
  type = c("bralette", "sports", "laced","pushup"))
profile <- candidate.list[c(2,4,9,17,12,13,18,21,23,27,30,32,35),]
library("conjoint") # install.packages("conjoint") if necessary.
pref <- read.csv("~/Desktop/dataan_VS/replies.csv")
head(pref)
caModel(y=pref[1,], x=profile)
levels <- c("low", "average", "high", "VS", "Aerie", "CK", "bralette", "sports", "laced", "pushup")
caUtilities(y=pref[1,], x=profile, z=levels)
pworth <- caPartUtilities(y=pref, x=profile, z=levels)
write.csv(pworth, "~/Desktop/dataan_VS/partworths.csv", row.names = FALSE)
head(pworth)
Conjoint(y=pref, x=profile, z=levels)
im <- caImportance(y=pref, x=profile)
names(im) <- colnames(profile)
im
barplot(im,las=2,col=1:length(im),main="Attribute Importance") # las=2 makes label text perpendicular to axis
apw <- caUtilities(y=pref, x=profile, z=levels)
names(apw) = c('intercept', levels)
apw
barplot(apw[2:length(apw)],las=2,col=1:length(im),main="Average Part Worths (utils)")
tUtil <- as.data.frame(caTotalUtilities(y=pref, x=profile))
id <- c(1:100)
names(id) <- "id"
colnames(tUtil) <- colnames(pref)
tUtil <- cbind(id,tUtil)
head(tUtil)
write.csv(tUtil, "~/Desktop/dataan_VS/totalUtility.csv", row.names = FALSE)