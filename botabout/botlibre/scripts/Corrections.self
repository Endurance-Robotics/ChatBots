// Scripts can be used to give programmatic responses to patterns, or process state machines.
state Corrections {
//	pattern "(can) (you) tell me who * is" template redirect(Template("who is {star}"));
//	pattern "do you know who * is" template redirect(Template("who is {star}"));
//	pattern "tell me who * is" template redirect(Template("who is {star}"));
//	
//	pattern "what do you [think know] [about of] *" template redirect(Template("what is {star}"));
//	pattern "I [want would] (like) to know (something anything everything) (about) *" template redirect(Template("what is {star}"));
//	pattern "(can) (you) tell me what * is" template redirect(Template("what is {star}"));
//	pattern "(what) (can) (you) tell me (something anything everything) about *" template redirect(Template("what is {star}"));
//	pattern "do you know what * is" template redirect(Template("what is {star}"));
//	pattern "do you know (something anything everything) about *" template redirect(Template("what is {star}"));
//	pattern "* is what" template redirect(Template("what is {star}"));	
//	pattern "what does * mean" template redirect(Template("what is {star}"));
//	pattern "what does it mean to be *" template redirect(Template("what is {star}"));
//	
//	pattern "do you [know think remember] (that) *" template redirect(Template("{star}?"));
//	pattern "remember (that) *" template redirect(star);
//	pattern "please *" template redirect(star);
//	pattern "pls *" template redirect(star);
//	
//	pattern "where in the world is *" template redirect(Template("where is {star}"));

	pattern "*--*" template redirect(Template("{star[0]}-{star[1]}"));

	pattern "*чатбот*" template redirect(Template("{star[0]}чат-бот{star[1]}"));
	pattern "*чатбота*" template redirect(Template("{star[0]}чат-бота{star[1]}"));
	pattern "*чатботу*" template redirect(Template("{star[0]}чат-боту{star[1]}"));
	pattern "*чатботом*" template redirect(Template("{star[0]}чат-ботом{star[1]}"));
	pattern "*чатботе*" template redirect(Template("{star[0]}чат-боте{star[1]}"));
	pattern "*чатботы*" template redirect(Template("{star[0]}чат-боты{star[1]}"));
	pattern "*чатботов*" template redirect(Template("{star[0]}чат-ботов{star[1]}"));
	pattern "*чатботам*" template redirect(Template("{star[0]}чат-ботам{star[1]}"));
	pattern "*чатботами*" template redirect(Template("{star[0]}чат-ботами{star[1]}"));
	pattern "*чатботах*" template redirect(Template("{star[0]}чат-ботах{star[1]}"));

	pattern "*может быть*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*наверное*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*я (так) думаю*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*я хочу (чтобы)*" template redirect(Template("{star[0]}{star[1]}"));

	pattern "*ты*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*тебя*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*твое*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*твоё*" template redirect(Template("{star[0]}{star[1]}"));

	pattern "*своими*" template redirect(Template("{star[0]}{star[1]}"));

	pattern "*скажи*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*сказать*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*ответь*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*ответить*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*расскажи*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*рассказать*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*напиши*" template redirect(Template("{star[0]}{star[1]}"));
	pattern "*написать*" template redirect(Template("{star[0]}{star[1]}"));

	pattern "*кто такой*" template redirect(Template("{star[0]}кто{star[1]}"));

	pattern "*ghbdtn*" template redirect(Template("{star[0]}привет{star[1]}"));
	pattern "*прива*" template redirect(Template("{star[0]}привет{star[1]}"));
	pattern "*пвет*" template redirect(Template("{star[0]}привет{star[1]}"));
	pattern "*приветт*" template redirect(Template("{star[0]}привет{star[1]}"));
}
