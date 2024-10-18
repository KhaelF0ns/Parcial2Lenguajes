// Generated from /home/khaelf0ns/Documents/Parcial2Lenguajes/mapFilter/mapFilter.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link mapFilterParser}.
 */
public interface mapFilterListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(mapFilterParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(mapFilterParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(mapFilterParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(mapFilterParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#mapFunction}.
	 * @param ctx the parse tree
	 */
	void enterMapFunction(mapFilterParser.MapFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#mapFunction}.
	 * @param ctx the parse tree
	 */
	void exitMapFunction(mapFilterParser.MapFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#filterFunction}.
	 * @param ctx the parse tree
	 */
	void enterFilterFunction(mapFilterParser.FilterFunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#filterFunction}.
	 * @param ctx the parse tree
	 */
	void exitFilterFunction(mapFilterParser.FilterFunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#lambdaExpr}.
	 * @param ctx the parse tree
	 */
	void enterLambdaExpr(mapFilterParser.LambdaExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#lambdaExpr}.
	 * @param ctx the parse tree
	 */
	void exitLambdaExpr(mapFilterParser.LambdaExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(mapFilterParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(mapFilterParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#op}.
	 * @param ctx the parse tree
	 */
	void enterOp(mapFilterParser.OpContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#op}.
	 * @param ctx the parse tree
	 */
	void exitOp(mapFilterParser.OpContext ctx);
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#iterable}.
	 * @param ctx the parse tree
	 */
	void enterIterable(mapFilterParser.IterableContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#iterable}.
	 * @param ctx the parse tree
	 */
	void exitIterable(mapFilterParser.IterableContext ctx);
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#list}.
	 * @param ctx the parse tree
	 */
	void enterList(mapFilterParser.ListContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#list}.
	 * @param ctx the parse tree
	 */
	void exitList(mapFilterParser.ListContext ctx);
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#tuple}.
	 * @param ctx the parse tree
	 */
	void enterTuple(mapFilterParser.TupleContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#tuple}.
	 * @param ctx the parse tree
	 */
	void exitTuple(mapFilterParser.TupleContext ctx);
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#elements}.
	 * @param ctx the parse tree
	 */
	void enterElements(mapFilterParser.ElementsContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#elements}.
	 * @param ctx the parse tree
	 */
	void exitElements(mapFilterParser.ElementsContext ctx);
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#var}.
	 * @param ctx the parse tree
	 */
	void enterVar(mapFilterParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#var}.
	 * @param ctx the parse tree
	 */
	void exitVar(mapFilterParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by {@link mapFilterParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(mapFilterParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link mapFilterParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(mapFilterParser.ExprContext ctx);
}