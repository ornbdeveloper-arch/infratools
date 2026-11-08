from fastapi import FastAPI, Request
from web.routes.hardware import router as hardware_router
from web.routes.system import router as system_router
from web.routes.network import router as network_router
from web.routes.processes import router as processes_router

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="web/templates")

app = FastAPI(
    title="InfraTools",
    description="Ferramenta de diagnóstico e monitoramento de infraestrutura",
    version="1.0.0"
)

app.mount(
    "/static",
    StaticFiles(directory="web/static"),
    name="static"
)

app.include_router(hardware_router, prefix="/api")
app.include_router(system_router, prefix="/api")
app.include_router(network_router, prefix="/api")
app.include_router(processes_router, prefix="/api")

@app.get('/')
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={'request': request}
    )
    

