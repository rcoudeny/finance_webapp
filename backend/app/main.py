
from fastapi import FastAPI
from api.routes.api import router as api_router
from core.config import PROJECT_NAME, VERSION, API_PREFIX, ALLOWED_HOSTS
from starlette.middleware.cors import CORSMiddleware



def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, # debug=DEBUG, 
        version=VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # application.add_event_handler("startup", create_start_app_handler(application))
    # application.add_event_handler("shutdown", create_stop_app_handler(application))

    # application.add_exception_handler(HTTPException, http_error_handler)
    # application.add_exception_handler(RequestValidationError, http422_error_handler)

    application.include_router(api_router, prefix=API_PREFIX)

    return application


app = get_application()



