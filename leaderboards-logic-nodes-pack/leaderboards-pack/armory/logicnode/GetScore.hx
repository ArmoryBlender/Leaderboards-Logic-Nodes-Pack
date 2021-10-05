package armory.logicnode;

import haxe.Json;
import iron.data.Data;
import armory.logicnode.LogicTree;
import armory.logicnode.LogicNode;


class GetScore extends LogicNode {

	var file:String = 'Leaderboards.json';

    public function new(tree:LogicTree) {
        super(tree);
       
    }

    override function get(from:Int):Dynamic {
        var data = getContent().leaderboard[0];

        if (from == 0) {
            return data.name;
        } else {
            return data.score;
        }
    }

    function getContent():Dynamic {
		var data:Dynamic;

		Data.getBlob(file, (blob) -> {
			data = Json.parse(blob.toString());
			Data.cachedBlobs.remove(file);
		});

		return data;
	}
}