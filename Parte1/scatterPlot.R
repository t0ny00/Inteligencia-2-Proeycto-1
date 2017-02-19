data = read.table("x01-data-30Iter.txt")
weights = read.table("x01-weights-30Iter.txt")
plot(data$V2,data$V3,type = "p",pch = 19, col="blue",
    xlab = "Brain Weight (normalized, unknown cale)",
    ylab = "Body Weight (normalized, unknown cale)",
    main = expression(paste("Weight relation between brain and body among mammals")),
    panel.first = grid())
legend(x = 5, y = 1, 
       legend = "Regression line",
       col = c("red"),
       pch="-",
       cex = 0.75)
abline(a= weights$V1,b= weights$V2, col = "red")
