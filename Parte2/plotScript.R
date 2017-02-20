
cost1 = read.table("x08-costFunct-30Iter-0.1.txt")
cost2 = read.table("x08-costFunct-30Iter-0.3.txt")
cost3 = read.table("x08-costFunct-30Iter-0.5.txt")
cost4 = read.table("x08-costFunct-30Iter-0.7.txt")
cost5 = read.table("x08-costFunct-30Iter-0.9.txt")
cost6 = read.table("x08-costFunct-30Iter-1.0.txt")
plot(cost1,type = "l", col="red",lwd=2,
    xlab = "Number of Iterations",
    ylab = "Cost Function Value",
    main = expression(paste("Convergence Curve for Several ",alpha, " Values")),
    panel.first = grid())
legend(x = 23, y = 0.5, 
       legend = c(expression(paste(alpha, "= 0.1")),
                  expression(paste(alpha, "= 0.3")),
                  expression(paste(alpha, "= 0.5")),
                  expression(paste(alpha, "= 0.7")),
                  expression(paste(alpha, "= 0.9")),
                  expression(paste(alpha, "= 1.0"))),
       col = c("red","blue","green","cyan","purple","grey"),
       pch=16)
lines(cost2, col="blue",lwd=2)
lines(cost3, col="green",lwd=2)
lines(cost4, col="cyan",lwd=2)
lines(cost5, col="purple",lwd=2)
lines(cost6, col="grey",lwd=2)

plot(cost1,type = "l", col="red",lwd=2,
     xlab = "Number of Iterations",
     ylab = "Cost Function Value",
     main = expression(paste("Convergence Curve for ",alpha, "= 0.1")),
     panel.first = grid())
