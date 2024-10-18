from mapFilterVisitor import mapFilterVisitor
from mapFilterParser import mapFilterParser


class MyVisitor(mapFilterVisitor):
    def visitMapFunction(self, ctx):
        function_expr = ctx.lambdaExpr().getText()

        # Procesar cada iterable por separado
        iterable_elements = []
        for iterable in ctx.iterable():
            result = iterable.accept(self)
            print(result)
            if result is not None:
                iterable_elements.append(result)

        # Combinar los elementos de los iterables
        combined_elements = list(zip(*iterable_elements))

        # Reemplazar 'lambda' para que Python lo reconozca
        function_expr = function_expr.replace("lambda", "lambda ")

        # Usar eval para aplicar la función al iterable combinado
        # Desempaquetar los elementos combinados para pasar a la función lambda
        result = [eval(function_expr)(*args) for args in combined_elements]
        print(result)
        return result



    def visitFilterFunction(self, ctx):
        function_expr = ctx.lambdaExpr().getText()

        # Procesar cada iterable por separado
        iterable_elements = []
        for iterable in ctx.iterable():
            result = iterable.accept(self)
            if result is not None:
                iterable_elements.append(result)

        # Combinar los elementos de los iterables
        combined_elements = list(zip(*iterable_elements))

        # Reemplazar 'lambda' para que Python lo reconozca
        function_expr = function_expr.replace("lambda", "lambda ")

        # Usar eval para filtrar el iterable combinado
        result = [args for args in combined_elements if eval(function_expr)(*args)]
        print(result)
        return result


    def visitList(self, ctx):
        # Esta función maneja la conversión de la lista desde la gramática
        elements = ctx.elements().accept(self)
        return elements

    def visitElements(self, ctx):
        if ctx.expr():
            return [ctx.expr(i).accept(self) for i in range(len(ctx.expr()))]
        else:
            return [ctx.iterable(i).accept(self) for i in range(len(ctx.iterable()))]

    def visitExpr(self, ctx):
        # Convertir la expresión a su tipo correspondiente
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')

