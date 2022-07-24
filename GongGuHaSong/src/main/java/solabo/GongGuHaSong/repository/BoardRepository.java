package solabo.GongGuHaSong.repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import solabo.GongGuHaSong.domain.Board;

public interface BoardRepository extends MongoRepository<Board,String> {
}
