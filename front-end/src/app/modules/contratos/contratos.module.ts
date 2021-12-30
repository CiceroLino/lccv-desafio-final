import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ContratosRoutingModule } from './contratos-routing.module';
import { IndexComponent } from './components/index/index.component';
import { CreateComponent } from './components/create/create.component';


@NgModule({
  declarations: [
    IndexComponent,
    CreateComponent
  ],
  imports: [
    CommonModule,
    ContratosRoutingModule
  ]
})
export class ContratosModule { }
