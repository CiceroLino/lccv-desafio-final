import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [

  {
    path: 'contratos',
    loadChildren: () => import ('./modules/contratos/contratos.module')
      .then( m => m.ContratosModule)
  },
  {
    path: 'listar',
    loadChildren: () => import ('./modules/listar/listar.module')
      .then( m => m.ListarModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
