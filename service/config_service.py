from sqlalchemy.orm import Session

from model import Coze, WorkFlow


def get_coze(DB):
    with DB.session(autoflush=True, autobegin=True) as session:
        _cozes = session.query(Coze).filter_by(is_delete=False).all()
        return [c.as_dict() for c in _cozes]


def get_work_flow(DB):
    with DB.session(autoflush=True, autobegin=True) as session:
        _work_flows = session.query(WorkFlow).filter_by(is_delete=False).all()
        return [w.as_dict() for w in _work_flows]


def update_coze(DB, coze_id, new_coze_key):
    with DB.session(autoflush=False, autobegin=False) as session:
        with session.begin() as transaction:
            _session: Session = session
            _coze = session.query(Coze).filter_by(id=coze_id).first()
            _coze.key = new_coze_key
            _session.flush()

def new_coze(DB, name ,new_coze_key):
    with DB.session(autoflush=False, autobegin=False) as session:
        with session.begin() as transaction:
            _session: Session = session
            _new_coze = Coze(name=name, key=new_coze_key)
            _session.add(_new_coze)
            _session.flush()
            return [coze.as_dict() for coze in session.query(Coze).filter_by(is_delete=False).all()]


def new_work_flow(DB, name, new_work_flow_id):
    with DB.session(autoflush=False, autobegin=False) as session:
        with session.begin() as transaction:
            _session: Session = session
            _new_work_flow = WorkFlow(name=name, workflow_id=new_work_flow_id)
            _session.add(_new_work_flow)
            _session.flush()
            return [work_flow.as_dict() for work_flow in session.query(WorkFlow).filter_by(is_delete=False).all()]
