import { MutationTree } from "vuex";
import { BoardState, Board } from "./states";
import { 
    REQUEST_BOARD_TO_DJANGO,
    REQUEST_BOARD_LIST_TO_DJANGO 
} from "./mutation-types";

export interface BoardMutations extends MutationTree<BoardState> {
    [REQUEST_BOARD_TO_DJANGO] (state: BoardState, receivedData: Board): void
    [REQUEST_BOARD_LIST_TO_DJANGO] (state: BoardState, receivedData: Board[]): void
}

const mutations: MutationTree<BoardState> = {
    [REQUEST_BOARD_TO_DJANGO] (state: BoardState, receivedData: Board): void {
        state.board = receivedData
    },
    [REQUEST_BOARD_LIST_TO_DJANGO] (state: BoardState, receivedData: Board[]): void {
        state.boards = receivedData
    }
}

// 현재 Board Domain 만 다루고 있기 때문에 사실 아래와 같은 작업이 필요 없음
// 그러나 앞으로 추가할 것들을 고려한다면 예약어인 mutations를 피해야합니다.
// 고로 as를 사용하여 Board Domain 전용 Mutations라는 것을 표기하였습니다.
// mutations를 BoardMutations라 다시 이름을 명명한이유
// mutations는 예약어라 여러 도메인에 쓰일 시 분간이 안 되기 때문에
// Board에서만 쓰일 예약어라고 명명
export default mutations as BoardMutations