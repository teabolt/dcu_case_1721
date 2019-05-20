fishn = 20
sharkn = 5
months = 3000
area = 10000
shark_die = 0.01
x = c()
y = c()

despawn_shark <- function(sharkn){
    despawns = 0
    if (sharkn > 3){
        for (shark in c(1:sharkn)){
            
            if (runif(1) < shark_die){
                despawns = despawns + 1
            }
        }
    }
    return (sharkn - despawns)
}


spawn_fish <- function(fishn){
    spawns = 0
        for (fish in c(1:fishn)){
            if (runif(1)<0.01){
                spawns = spawns + 1
            }
        }
    
    return (spawns + fishn)
}



for (month in c(1:months)){
    fishn = spawn_fish(fishn)
    sharkn = despawn_shark(sharkn)
    for (fish in c(1:fishn)){
        if (runif(1) < sharkn/area){
            fishn = fishn - 1
                sharkn = sharkn + 1
            
        }
    }
    x[month] = fishn
    y[month] = sharkn
    print(fishn)
    print(sharkn)
    plot(x,xlab="Months",ylab="Fish Population")
    points(y,col="blue")
    Sys.sleep(0.01)
}
