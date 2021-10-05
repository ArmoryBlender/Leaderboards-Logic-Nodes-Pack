package armory.logicnode;

import haxe.io.Bytes;
import armory.logicnode.LogicTree;
import armory.logicnode.LogicNode;


class ResetScore extends LogicNode {

    var path:String = '';
    var file:String = 'Leaderboards.json';

    public function new(tree:LogicTree) {
        super(tree);
        #if kha_krom
		path = Krom.getFilesLocation() + "/../../../Bundled/" + file;
		#end
    }

    override function run(from:Int) {
        save('{ "leaderboard" : [{"name" : "noname", "score": "0"}] }');


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