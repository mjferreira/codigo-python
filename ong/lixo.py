    def imprimir_linha_tabela(self, pdf, texto, y, fonte="Helvetica-Bold", tamanho=16, posicao=0, largura_coluna=0, fundo=colors.white):
        """ Centraliza um texto horizontalmente no PDF """
        pdf.setFillColor(fundo)    
        y1 =  self.altura_pagina-self.mp(y)
        y2 =  self.altura_pagina-self.mp(y-2)     
        if posicao == 0:
            # Calcula a posição X centralizada
            largura_texto = pdf.stringWidth(texto, fonte, tamanho)
            largura_coluna = self.largura_pagina-(2*self.mp(20))
            x = (self.largura_pagina - largura_texto) / 2
            posicao = self.mp(20)
        else:
            x = posicao+self.mp(2)
        
        pdf.rect(posicao, y1, largura_coluna, altura_coluna, fill=1)  # Preencher o retângulo                                               
        pdf.setFillColor(colors.black) 
        pdf.setFont(fonte, tamanho)   
        # Desenha o texto na posição centralizada
        pdf.drawString(x, y2, texto)       
       
    def imprimir_texto(self, pdf, texto, y, fonte="Helvetica-Bold", tamanho=16, posicao=0):
        """ Centraliza um texto horizontalmente no PDF """      
        if posicao == 0:
            # Calcula a posição X centralizada
            largura_texto = pdf.stringWidth(texto, fonte, tamanho)
            x = (self.largura_pagina - largura_texto) / 2
        else:
            x = posicao
        
        pdf.setFont(fonte, tamanho)   
        # Desenha o texto na posição centralizada
        pdf.drawString(x, y, texto)