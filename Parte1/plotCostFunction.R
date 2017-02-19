cost1 = read.table("x01-costFunct-30Iter-0.1.txt")
plot(cost1,type = "l", col="red",lwd=2,
    xlab = "Number of Iterations",
    ylab = "Cost Function Value",
    main = expression(paste("Convergence Curve for ",alpha, "=0.1")),
    panel.first = grid())
