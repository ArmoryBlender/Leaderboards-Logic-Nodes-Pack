package armory.logicnode;

import haxe.io.Bytes;
import armory.logicnode.LogicTree;
import armory.logicnode.LogicNode;


class AddScore extends LogicNode {

    var path:String = '';
    var file:String = 'Leaderboards.json';

    public function new(tree:LogicTree) {
        super(tree);
        #if kha_krom
		path = Krom.getFilesLocation() + "/../../../Bundled/" + file;
		#end
    }

    override function run(from:Int) {
        var name:String = inputs[1].get();
        var score:Float = inputs[2].get();

        var user:User = {
            username: name,
            userscore: score
        }



        save('{ "leaderboard" : [{"name" : "$name", "score": $score}] }');


        runOutput(0);
    }

    function save(data:String) {
		#if kha_krom
		var bytes = Bytes.ofString(data);
		Krom.fileSaveBytes(path, bytes.getData());
		#end

		trace('Content saved!!');
	}
}

typedef User = {
	var username:String;
	var userscore:Float;
	@:optional var time:Float;
}