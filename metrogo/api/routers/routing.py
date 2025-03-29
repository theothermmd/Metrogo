from fastapi import APIRouter
from fastapi.responses import JSONResponse
from metrogo.services.Routing import find_best_route

router = APIRouter()


@router.get('/get_route')
async def get_route(
	source: str,
	destination: str,
	type_of_day: str | None = 'عادی',
	time: str | None = None,
):
	try:
		return JSONResponse(
			status_code=200,
			content=find_best_route(
				source=source,
				destination=destination,
				type_day=type_of_day,
				current_time_str=time,
			),
		)
	except Exception as error:
		return JSONResponse(status_code=500, content={'message': error})
