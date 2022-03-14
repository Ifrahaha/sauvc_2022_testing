C = 100 ;
    for (i = 1; i < n; i++) {
        for (j = 1; j < n; j++) { 
            Temp = A[i][j] + C 
            A[i][j] = A[j][i] 
            
            A[j][1] = Temp - C } }
            for (i = 1; i < n; i++) { 
                for (j = 1; j < n; j++) 
                printf("%d",A[i][j]); 
                printf("\n"); 